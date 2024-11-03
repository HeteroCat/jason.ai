import streamlit as st
import requests
import json

# 设置页面配置
st.set_page_config(page_title="Dify 007Chatbot", page_icon="💬")

# 侧边栏配置
with st.sidebar:
    api_key = st.text_input("Dify API Key", key="chatbot_api_key", type="password")
    

# 主标题
st.title("💬 Dify 007Chatbot")
st.caption("🚀 A streamlit chatbot powered by Dify AI")

# 初始化会话状态
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "你好! 你知道的我不好惹?"}]

if "conversation_id" not in st.session_state:
    st.session_state.conversation_id = None

# 显示聊天历史
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 聊天输入和处理
if prompt := st.chat_input("What would you like to know?"):
    if not api_key:
        st.info("Please add your Dify API key to continue.")
        st.stop()

    # 添加用户消息到界面
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 准备发送到Dify API的请求
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }

    # 构建请求数据
    data = {
        "inputs": {},
        "query": prompt,
        "response_mode": "blocking",
        "user": "user-123",
    }

    # 如果存在对话ID，添加到请求中
    if st.session_state.conversation_id:
        data["conversation_id"] = st.session_state.conversation_id

    try:
        # 发送请求到Dify API
        response = requests.post(
            'https://api.dify.ai/v1/chat-messages',
            headers=headers,
            json=data
        )

        if response.status_code == 200:
            result = response.json()
            
            # 保存对话ID
            if result.get('conversation_id'):
                st.session_state.conversation_id = result['conversation_id']

            # 获取AI响应
            assistant_response = result.get('answer', 'Sorry, I could not generate a response.')
            
            # 添加助手响应到消息历史
            st.session_state.messages.append({"role": "assistant", "content": assistant_response})
            
            # 显示助手响应
            with st.chat_message("assistant"):
                st.markdown(assistant_response)
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    
    except requests.exceptions.RequestException as e:
        st.error(f"Error occurred: {str(e)}")

# 添加重置按钮到侧边栏
with st.sidebar:
    if st.button("Reset Conversation"):
        st.session_state.messages = [{"role": "assistant", "content": "你好! 你知道的我不好惹?"}]
        st.session_state.conversation_id = None
        st.rerun()