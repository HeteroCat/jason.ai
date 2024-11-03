import openai
import streamlit as st


with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")


st.title("💬 game Chatbot")
st.caption("🚀 A streamlit chatbot powered by OpenAI LLM")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": " let's start the journey of the text game!"}]

# for msg in st.session_state.messages:
#     st.chat_message(msg["role"]).write(msg["content"])
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        
        st.markdown(message["content"])
if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    openai.api_key = openai_api_key
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)

# 添加重置按钮到侧边栏
with st.sidebar:
    if st.button("Reset Conversation"):
        st.session_state.messages = [{"role": "assistant", "content": "let's start the journey of the text game!"}]
        st.session_state.conversation_id = None
        st.rerun()