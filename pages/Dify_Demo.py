import streamlit as st
import requests

# 设置页面配置
st.set_page_config(page_title="Dify 007Chatbot", page_icon="💬")

# 页面标识
PAGE_ID = "dify_chat"

# 初始化状态
if f"{PAGE_ID}_messages" not in st.session_state:
    st.session_state[f"{PAGE_ID}_messages"] = [{"role": "assistant", "content": "你好! 你知道的我不好惹?"}]

if f"{PAGE_ID}_conversation_id" not in st.session_state:
    st.session_state[f"{PAGE_ID}_conversation_id"] = None

# 快捷访问 session_state 的键
messages = st.session_state[f"{PAGE_ID}_messages"]
conversation_id = st.session_state[f"{PAGE_ID}_conversation_id"]

# 嵌入 API Key（直接硬编码）
API_KEY = "app-ZQZYF6F5o3cDFugpWjkZjPql"

# 主标题
st.title("💬 Dify 007Chatbot")
st.caption("🚀 A Streamlit chatbot powered by Dify")

# 显示消息历史
for message in messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 聊天输入和处理
if prompt := st.chat_input("What would you like to know?"):
    if not API_KEY:
        st.error("API Key is missing. Please check the code.")
        st.stop()

    # 添加用户消息到界面和历史记录
    messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 准备发送到 Dify API 的请求
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json',
    }

    data = {
        "inputs": {},
        "query": prompt,
        "response_mode": "blocking",
        "user": "user-123",
    }

    if conversation_id:
        data["conversation_id"] = conversation_id

    try:
        # 发送请求到 Dify API
        response = requests.post(
            'https://api.dify.ai/v1/chat-messages',
            headers=headers,
            json=data
        )

        if response.status_code == 200:
            result = response.json()
            # 更新对话ID
            st.session_state[f"{PAGE_ID}_conversation_id"] = result.get("conversation_id", conversation_id)
            assistant_response = result.get("answer", "Sorry, I could not generate a response.")
            
            # 添加助手响应到历史记录并显示
            messages.append({"role": "assistant", "content": assistant_response})
            with st.chat_message("assistant"):
                st.markdown(assistant_response)
        else:
            st.error(f"API Error: {response.status_code} - {response.text}")
            st.sidebar.text_area("Debug Info", f"{response.text}")

    except requests.exceptions.RequestException as e:
        st.error("An error occurred during the API request.")
        st.sidebar.text_area("Error Details", str(e))


# 修改重置按钮
with st.sidebar:
    if st.button("Reset Conversation"):
        st.session_state[f"{PAGE_ID}_messages"] = [{"role": "assistant", "content": "你好! 你知道的我不好惹?"}]
        st.session_state[f"{PAGE_ID}_conversation_id"] = None
        st.rerun()