import requests
import streamlit as st

import json
import time


# API 配置
BOT_ID = "7426248689075028006"
BASE_URL = "https://api.coze.cn/v3"

with st.sidebar:
    API_TOKEN = st.text_input("Coze API Token", key="coze_api_key", type="password")

# 发送聊天请求
def send_chat_request(question, api_token):
    url = f"{BASE_URL}/chat"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    data = {
        "bot_id": BOT_ID,
        "user_id": "12564489",  # 可以使用任意用户ID
        "stream": False,
        "auto_save_history": True,
        "additional_messages": [
            {
                "role": "user",
                "content": question,
                "content_type": "text"
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()


# 获取聊天消息
def get_chat_messages(chat_id, conversation_id, api_token):
    url = f"{BASE_URL}/chat/message/list?chat_id={chat_id}&conversation_id={conversation_id}"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)
    return response.json()

def main():
    st.title("💬AI 分身聊天机器人")
    st.write("🥰与我的coze分身智能体互动，询问问题并获取回复！")

    # 用户输入
    user_input = st.text_input("请输入问题：")

    if st.button("发送"):
        if not API_TOKEN:
            st.info("Please add your Coze API Token to continue.")
            st.stop()

        if user_input:
            with st.spinner('正在获取回应...'):
                chat_response = send_chat_request(user_input, API_TOKEN)
                st.json(chat_response)

                if "code" in chat_response and chat_response["code"] == 0 and "data" in chat_response:
                    chat_id = chat_response["data"].get("id")
                    conversation_id = chat_response["data"].get("conversation_id")

                    if chat_id and conversation_id:
                        # 尝试获取聊天消息，最多重试5次
                        for attempt in range(5):
                            print(f"尝试获取消息，第 {attempt + 1} 次")
                            messages = get_chat_messages(chat_id, conversation_id, API_TOKEN)

                            if "code" in messages and messages["code"] == 0 and "data" in messages and messages["data"]:
                                for message in messages["data"]:
                                    if message["role"] == "assistant" and message["type"] == "answer":
                                        st.write(f"智能体的回答：{message['content']}")
                                        return
                            time.sleep(5)  # 等待5秒后重试

                        st.write("已完成，但是由于streamlit cloud服务器在国外，所以扣子无法服务。本地运行已实现")
                    else:
                        st.write("chat_id 或 conversation_id 未在响应中找到")
                else:
                    st.write("发送聊天请求失败或返回格式不正确")
        else:
            st.warning("请输入一个问题")

if __name__ == "__main__":
    main()

