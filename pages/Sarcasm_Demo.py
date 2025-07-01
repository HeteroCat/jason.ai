import streamlit as st
import requests

# 设置页面配置
st.set_page_config(page_title="Sarcasm Chatbot", page_icon="💬")

# 页面标识
PAGE_ID = "sarcasm_chat"

# 初始化状态
if f"{PAGE_ID}_messages" not in st.session_state:
    st.session_state[f"{PAGE_ID}_messages"] = [{"role": "assistant", "content": "你好! 你知道的我不好惹?"}]

if f"{PAGE_ID}_conversation_id" not in st.session_state:
    st.session_state[f"{PAGE_ID}_conversation_id"] = None

# 快捷访问 session_state 的键
messages = st.session_state[f"{PAGE_ID}_messages"]
conversation_id = st.session_state[f"{PAGE_ID}_conversation_id"]

# 侧边栏配置
with st.sidebar:
    api_key = st.text_input("Dify API Key", key="chatbot_api_key", type="password")
    if st.button("Reset Conversation"):
        st.session_state[f"{PAGE_ID}_messages"] = [{"role": "assistant", "content": "你好! 你知道的我不好惹?"}]
        st.session_state[f"{PAGE_ID}_conversation_id"] = None
        st.rerun()

# 主标题
st.title("💬 Sarcasm Chatbot")
st.caption("🚀 A Streamlit chatbot powered by Dify AI")

# 显示消息历史
for message in messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 聊天输入和处理
if prompt := st.chat_input("What would you like to know?"):
    if not api_key:
        st.info("Please add your Dify API key to continue.")
        st.stop()

    # 添加用户消息到界面和历史记录
    messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 准备发送到 Dify API 的请求
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }

    data = {
        "inputs": {},
        "query": prompt,
        "response_mode": "blocking",
        "user": "user456",
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
