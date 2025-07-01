
import streamlit as st
import pandas as pd
import os
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain.tools.retriever import create_retriever_tool
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_community.embeddings import DashScopeEmbeddings
from langchain.chat_models import init_chat_model
from langchain_experimental.tools import PythonAstREPLTool
import matplotlib
matplotlib.use('Agg')
import os
from dotenv import load_dotenv 
load_dotenv(override=True)


# API密钥将通过侧边栏输入获取
# DeepSeek_API_KEY = os.getenv("DEEPSEEK_API_KEY")
# dashscope_api_key = os.getenv("DASHSCOPE_API_KEY")

# 设置环境变量
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# 页面配置
st.set_page_config(
page_title="Data-Demo",
page_icon="🤖",
layout="wide",
initial_sidebar_state="expanded"
)

# 自定义CSS样式
st.markdown("""
<style>
    /* 主题色彩 */
    :root {
        --primary-color: #1f77b4;
        --secondary-color: #ff7f0e;
        --success-color: #2ca02c;
        --warning-color: #ff9800;
        --error-color: #d62728;
        --background-color: #f8f9fa;
    }
    
    /* 隐藏默认的Streamlit样式 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* 标题样式 */
    .main-header {
        background: linear-gradient(90deg, #1f77b4, #ff7f0e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* 卡片样式 */
    .info-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin: 1rem 0;
        border-left: 4px solid var(--primary-color);
    }
    
    .success-card {
        background: linear-gradient(135deg, #e8f5e8, #f0f8f0);
        border-left: 4px solid var(--success-color);
    }
    
    .warning-card {
        background: linear-gradient(135deg, #fff8e1, #fffbf0);
        border-left: 4px solid var(--warning-color);
    }
    
    /* 按钮样式 */
    .stButton > button {
        background: linear-gradient(45deg, #1f77b4, #2196F3);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 2px 8px rgba(31, 119, 180, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(31, 119, 180, 0.4);
    }
    
    /* Tab样式 */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 0.5rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 60px;
        background-color: white;
        border-radius: 8px;
        padding: 0 24px;
        font-weight: 600;
        border: 2px solid transparent;
        transition: all 0.3s ease;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(45deg, #1f77b4, #2196F3);
        color: white !important;
        border: 2px solid #1f77b4;
    }
    
    /* 侧边栏样式 */
    .css-1d391kg {
        background: linear-gradient(180deg, #f8f9fa, #ffffff);
    }
    
    /* 文件上传区域 */
    .uploadedFile {
        background: #f8f9fa;
        border: 2px dashed #1f77b4;
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
        margin: 1rem 0;
    }
    
    /* 状态指示器 */
    .status-indicator {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.9rem;
    }
    
    .status-ready {
        background: #e8f5e8;
        color: #2ca02c;
        border: 1px solid #2ca02c;
    }
    
    .status-waiting {
        background: #fff8e1;
        color: #ff9800;
        border: 1px solid #ff9800;
    }
</style>
""", unsafe_allow_html=True)

# 初始化embeddings
def init_embeddings(api_key):
    return DashScopeEmbeddings(
        model="text-embedding-v1", 
        dashscope_api_key=api_key
    )

# 初始化LLM
def init_llm(api_key):
    os.environ["DEEPSEEK_API_KEY"] = api_key
    return init_chat_model("deepseek-chat", model_provider="deepseek")

# 初始化会话状态
def init_session_state():
    if 'pdf_messages' not in st.session_state:
        st.session_state.pdf_messages = []
    if 'csv_messages' not in st.session_state:
        st.session_state.csv_messages = []
    if 'df' not in st.session_state:
        st.session_state.df = None

# PDF处理函数
def pdf_read(pdf_doc):
    text = ""
    for pdf in pdf_doc:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_text(text)
    return chunks

def vector_store(text_chunks, dashscope_api_key):
    embeddings = init_embeddings(dashscope_api_key)
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_db")

def check_database_exists():
    return os.path.exists("faiss_db") and os.path.exists("faiss_db/index.faiss")

def get_pdf_response(user_question, deepseek_api_key, dashscope_api_key):
    if not check_database_exists():
        return "❌ 请先上传PDF文件并点击'Submit & Process'按钮来处理文档！"
    
    try:
        embeddings = init_embeddings(dashscope_api_key)
        llm = init_llm(deepseek_api_key)
        
        new_db = FAISS.load_local("faiss_db", embeddings, allow_dangerous_deserialization=True)
        retriever = new_db.as_retriever()
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", """你是AI助手，请根据提供的上下文回答问题，确保提供所有细节，如果答案不在上下文中，请说"答案不在上下文中"，不要提供错误的答案"""),
            ("placeholder", "{chat_history}"),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}"),
        ])
        
        retrieval_chain = create_retriever_tool(retriever, "pdf_extractor", "This tool is to give answer to queries from the pdf")
        agent = create_tool_calling_agent(llm, [retrieval_chain], prompt)
        agent_executor = AgentExecutor(agent=agent, tools=[retrieval_chain], verbose=True)
        
        response = agent_executor.invoke({"input": user_question})
        return response['output']
        
    except Exception as e:
        return f"❌ 处理问题时出错: {str(e)}"

# CSV处理函数
def get_csv_response(query: str, deepseek_api_key: str) -> str:
    if st.session_state.df is None:
        return "请先上传CSV文件"
    
    llm = init_llm(deepseek_api_key)
    locals_dict = {'df': st.session_state.df}
    tools = [PythonAstREPLTool(locals=locals_dict)]
    
    system = f"""Given a pandas dataframe `df` answer user's query.
    Here's the output of `df.head().to_markdown()` for your reference, you have access to full dataframe as `df`:
    ```
    {st.session_state.df.head().to_markdown()}
    ```
    Give final answer as soon as you have enough data, otherwise generate code using `df` and call required tool.
    If user asks you to make a graph, save it as `plot.png`, and output GRAPH:<graph title>.
    Example:
    ```
    plt.hist(df['Age'])
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.title('Age Histogram')
    plt.savefig('plot.png')
    ``` output: GRAPH:Age histogram
    Query:"""

    prompt = ChatPromptTemplate.from_messages([
        ("system", system),
        ("placeholder", "{chat_history}"),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ])

    agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    
    return agent_executor.invoke({"input": query})['output']

def main():
    init_session_state()
    
    # 侧边栏配置
    with st.sidebar:
        st.markdown("### 🔑 API 配置")
        deepseek_api_key = st.text_input("DeepSeek API Key", key="deepseek_api_key", type="password", help="请输入您的DeepSeek API密钥")
        dashscope_api_key = st.text_input("DashScope API Key", key="dashscope_api_key", type="password", help="请输入您的阿里云DashScope API密钥")
        
        if st.button("🗑️ 重置所有数据"):
            # 清除PDF数据库
            import shutil
            if os.path.exists("faiss_db"):
                shutil.rmtree("faiss_db")
            # 清除会话状态
            st.session_state.pdf_messages = []
            st.session_state.csv_messages = []
            st.session_state.df = None
            if os.path.exists('plot.png'):
                os.remove('plot.png')
            st.success("所有数据已重置")
            st.rerun()
    
    # 主标题已移除
    st.markdown('<div style="text-align: center; margin-bottom: 2rem; color: #666;">📊集PDF问答与数据分析于一体的智能助手</div>', unsafe_allow_html=True)
    
    # 检查API密钥
    if not deepseek_api_key or not dashscope_api_key:
        st.warning("⚠️ 请在侧边栏输入API密钥以使用所有功能")
    
    # 创建两个主要功能的标签页
    tab1, tab2 = st.tabs(["📄 PDF智能问答", "📊 CSV数据分析"])
    
    # PDF问答模块
    with tab1:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("### 💬 与PDF文档对话")
            
            # 显示数据库状态
            if check_database_exists():
                st.markdown('<div class="info-card success-card"><span class="status-indicator status-ready">✅ PDF数据库已准备就绪</span></div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="info-card warning-card"><span class="status-indicator status-waiting">⚠️ 请先上传并处理PDF文件</span></div>', unsafe_allow_html=True)
            
            # 聊天界面
            for message in st.session_state.pdf_messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])
            
            # 用户输入
            if pdf_query := st.chat_input("💭 向PDF提问...", disabled=not check_database_exists() or not deepseek_api_key or not dashscope_api_key):
                if not deepseek_api_key or not dashscope_api_key:
                    st.error("❌ 请先在侧边栏输入API密钥")
                else:
                    st.session_state.pdf_messages.append({"role": "user", "content": pdf_query})
                    with st.chat_message("user"):
                        st.markdown(pdf_query)
                    
                    with st.chat_message("assistant"):
                        with st.spinner("🤔 AI正在分析文档..."):
                            response = get_pdf_response(pdf_query, deepseek_api_key, dashscope_api_key)
                        st.markdown(response)
                        st.session_state.pdf_messages.append({"role": "assistant", "content": response})
        
        with col2:
            st.markdown("### 📁 文档管理")
            
            # 文件上传
            pdf_docs = st.file_uploader(
                "📎 上传PDF文件",
                accept_multiple_files=True,
                type=['pdf'],
                help="支持上传多个PDF文件"
            )
            
            if pdf_docs:
                st.success(f"📄 已选择 {len(pdf_docs)} 个文件")
                for i, pdf in enumerate(pdf_docs, 1):
                    st.write(f"• {pdf.name}")
            
            # 处理按钮
            if st.button("🚀 上传并处理PDF文档", disabled=not pdf_docs or not dashscope_api_key, use_container_width=True):
                if not dashscope_api_key:
                    st.error("❌ 请先在侧边栏输入DashScope API密钥")
                else:
                    with st.spinner("📊 正在处理PDF文件..."):
                        try:
                            raw_text = pdf_read(pdf_docs)
                            if not raw_text.strip():
                                st.error("❌ 无法从PDF中提取文本")
                                return
                            
                            text_chunks = get_chunks(raw_text)
                            st.info(f"📝 文本已分割为 {len(text_chunks)} 个片段")
                            
                            vector_store(text_chunks, dashscope_api_key)
                            st.success("✅ PDF处理完成！")
                            st.balloons()
                            st.rerun()
                            
                        except Exception as e:
                            st.error(f"❌ 处理PDF时出错: {str(e)}")
            
            # 清除数据库
            if st.button("🗑️ 清除PDF数据库", use_container_width=True):
                try:
                    import shutil
                    if os.path.exists("faiss_db"):
                        shutil.rmtree("faiss_db")
                    st.session_state.pdf_messages = []
                    st.success("数据库已清除")
                    st.rerun()
                except Exception as e:
                    st.error(f"清除失败: {e}")
    
    # CSV数据分析模块
    with tab2:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("### 📈 数据分析对话")
            
            # 显示数据状态
            if st.session_state.df is not None:
                st.markdown('<div class="info-card success-card"><span class="status-indicator status-ready">✅ 数据已加载完成</span></div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="info-card warning-card"><span class="status-indicator status-waiting">⚠️ 请先上传CSV文件</span></div>', unsafe_allow_html=True)
            
            # 聊天界面
            for message in st.session_state.csv_messages:
                with st.chat_message(message["role"]):
                    if message["type"] == "dataframe":
                        st.dataframe(message["content"])
                    elif message["type"] == "image":
                        st.write(message["content"])
                        if os.path.exists('plot.png'):
                            st.image('plot.png')
                    else:
                        st.markdown(message["content"])
            
            # 用户输入
            if csv_query := st.chat_input("📊 分析数据...", disabled=st.session_state.df is None or not deepseek_api_key):
                if not deepseek_api_key:
                    st.error("❌ 请先在侧边栏输入DeepSeek API密钥")
                else:
                    st.session_state.csv_messages.append({"role": "user", "content": csv_query, "type": "text"})
                    with st.chat_message("user"):
                        st.markdown(csv_query)
                    
                    with st.chat_message("assistant"):
                        with st.spinner("🔄 正在分析数据..."):
                            response = get_csv_response(csv_query, deepseek_api_key)
                        
                        if isinstance(response, pd.DataFrame):
                            st.dataframe(response)
                            st.session_state.csv_messages.append({"role": "assistant", "content": response, "type": "dataframe"})
                        elif "GRAPH" in str(response):
                            text = str(response)[str(response).find("GRAPH")+6:]
                            st.write(text)
                            if os.path.exists('plot.png'):
                                st.image('plot.png')
                            st.session_state.csv_messages.append({"role": "assistant", "content": text, "type": "image"})
                        else:
                            st.markdown(response)
                            st.session_state.csv_messages.append({"role": "assistant", "content": response, "type": "text"})
        
        with col2:
            st.markdown("### 📊 数据管理")
            
            # CSV文件上传
            csv_file = st.file_uploader("📈 上传CSV文件", type='csv')
            if csv_file:
                st.session_state.df = pd.read_csv(csv_file)
                st.success(f"✅ 数据加载成功!")
                
                # 显示数据预览
                with st.expander("👀 数据预览", expanded=True):
                    st.dataframe(st.session_state.df.head())
                    st.write(f"📏 数据维度: {st.session_state.df.shape[0]} 行 × {st.session_state.df.shape[1]} 列")
            
            # 数据信息
            if st.session_state.df is not None:
                if st.button("📋 显示数据信息", use_container_width=True):
                    with st.expander("📊 数据统计信息", expanded=True):
                        st.write("**基本信息:**")
                        st.text(f"行数: {st.session_state.df.shape[0]}")
                        st.text(f"列数: {st.session_state.df.shape[1]}")
                        st.write("**列名:**")
                        st.write(list(st.session_state.df.columns))
                        st.write("**数据类型:**")
                        # 修复：将dtypes转换为字符串格式显示
                        dtype_info = pd.DataFrame({
                            '列名': st.session_state.df.columns,
                            '数据类型': [str(dtype) for dtype in st.session_state.df.dtypes]
                        })
                        st.dataframe(dtype_info, use_container_width=True)
            
            # 清除数据
            if st.button("🗑️ 清除CSV数据", use_container_width=True):
                st.session_state.df = None
                st.session_state.csv_messages = []
                if os.path.exists('plot.png'):
                    os.remove('plot.png')
                st.success("数据已清除")
                st.rerun()
    
    # 底部信息
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**🔧 技术栈:**")
        st.markdown("• LangChain • Streamlit • FAISS • DeepSeek")
    with col2:
        st.markdown("**✨ 功能特色:**")
        st.markdown("• PDF智能问答 • 数据可视化分析")
    with col3:
        st.markdown("**💡 使用提示:**")
        st.markdown("• 支持多文件上传 • 实时对话交互")

if __name__ == "__main__":
    main()
