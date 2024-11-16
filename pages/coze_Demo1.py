import requests
import streamlit as st
import time
# Streamlit侧边栏输入API Key
with st.sidebar:
    coze_api_key = st.text_input("Coze API Key", key="chatbot_api_key", type="password")

st.title("💬 HeteroCat Chatbot")
st.caption("🚀 A Streamlit chatbot powered by Coze API")

# 在文件开头添加页面标识
PAGE_ID = "coze_chat"

# 修改状态键名
# 初始化会话状态
if f"{PAGE_ID}_messages" not in st.session_state:
    st.session_state[f"{PAGE_ID}_messages"] = [{"role": "assistant", "content": "Let's start the journey of the text game!"}]



# 获取用户消息并进行对话
if prompt := st.chat_input():
    st.session_state[f"{PAGE_ID}_messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)


    # 进行 chat 对话请求
    chat_url = f"https://api.coze.cn/v3/chat"
    headers = {  # 确保 headers 在此处定义
        "Authorization": f"Bearer {coze_api_key}",
        "Content-Type": "application/json"
    }
    chat_data = {
        "bot_id": "7426248689075028006",  # 请替换为实际的 bot_id
        "user_id": "154643545",
        "stream": False,
        "auto_save_history": True,
        "additional_messages": [{"role": "user", "content": prompt, "content_type": "text"}]
    }

    # 发送对话请求
    chat_response = requests.post(chat_url, headers=headers, json=chat_data)
    chat_result = chat_response.json()

    if chat_result.get("code") == 0:
        chat_id = chat_result.get("data")["id"]
        conversation_id = chat_result.get("data")["conversation_id"]
        retrieve_url = f"https://api.coze.cn/v3/chat/retrieve"
        headers = { 
            "Authorization": f"Bearer {coze_api_key}",
            "Content-Type": "application/json"
        }
        # 查看对话详情
        retrieve_params = {
            "conversation_id": conversation_id,
            "chat_id": chat_id,
        }
        retrieve_response = requests.get(retrieve_url, headers=headers, params=retrieve_params)
        
        




        chat_result = retrieve_response.json()
        msg = str(chat_result)
        st.session_state[f"{PAGE_ID}_messages"].append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)
    else:
        st.error("Failed to fetch chat response.")

    
# 重置按钮
with st.sidebar:
    if st.button("Reset Conversation"):
        st.session_state[f"{PAGE_ID}_messages"] = [{"role": "assistant", "content": "Hi，这里是HeteroCat异瞳猫。如果你对我和AI有任何感兴趣的话题，欢迎━(｀∀´)ノ亻!与我交流！！！"}]
        st.session_state.pop("conversation_id", None)
        st.rerun()
