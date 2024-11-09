import openai
import streamlit as st


with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")


st.title("💬 game Chatbot")
st.caption("🚀 A streamlit chatbot powered by OpenAI LLM")

# 在文件开头添加页面标识
PAGE_ID = "game_chat"

# 修改状态键名
if f"{PAGE_ID}_messages" not in st.session_state:
    st.session_state[f"{PAGE_ID}_messages"] = [{"role": "assistant", "content": "let's start the journey of the text game!"}]

# 修改后续使用
for message in st.session_state[f"{PAGE_ID}_messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 修改OpenAI调用部分
if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    openai.api_key = openai_api_key
    st.session_state[f"{PAGE_ID}_messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=st.session_state[f"{PAGE_ID}_messages"]
    )
    msg = response.choices[0].message.content
    st.session_state[f"{PAGE_ID}_messages"].append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)

# 修改重置按钮
with st.sidebar:
    if st.button("Reset Conversation"):
        st.session_state[f"{PAGE_ID}_messages"] = [{"role": "assistant", "content": "let's start the journey of the text game!"}]
        st.rerun()