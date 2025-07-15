
import streamlit as st

st.set_page_config(page_title="AI网址导航", page_icon="🧠", layout="centered")

st.title("AI网址导航")

# 国外模型
st.header("🌍 国外模型")
st.markdown("""
- ☺️ [ChatGPT](https://chat.openai.com)
- 😂 [Claude](https://claude.ai)
- 😃 [Gemini](https://gemini.google.com)
""")

# 国内模型
st.header("🏠 国内模型")
st.markdown("""
- 😊 [Deepseek](https://deepseek.com)
- 😄 [豆包](https://www.doubao.com)
- 😆 [Kimi](https://kimi.moonshot.cn)
- 😇 [通义千问](https://qianwen.aliyun.com)
- 😝 [文心一言](https://yiyan.baidu.com)
- 😅 [讯飞星火](https://xinghuo.xfyun.cn)
- 😉 [腾讯元宝](https://yb.tencent.com)
- 😍 [智谱清言](https://chatglm.cn)
- 🫠 [百小应](https://xiaoying.baidu.com)
- 🫡 [零一万物](https://www.01.ai)
""")

# AIGC 平台
st.header("🎨 AIGC平台")
st.markdown("""
- 💪 [即梦](https://ji.moonshot.cn)
- 🦾 [可灵](https://kling.ai)
- 🫶 [Hidream](https://hidream.cn)
- 👏 [Haiper](https://haiper.ai)
- 👂 [SUNO](https://suno.com)
- 🦻 [天工](https://chat.tiangong.cn)
- 👀 [海螺](https://www.hailuoai.com)
- 🎀 [Runway](https://runwayml.com)
- 🎁 [Midjourney](https://www.midjourney.com)
- 🎟️ [tusiart](https://tusiart.com)
- ✨ [有言](https://youyan.baidu.com)
- 🎉 [稿定](https://www.gaoding.com)
- 🎐 [睿声](https://ruisheng.ai)
""")

# AI开发平台
st.header("🧑‍💻 AI开发平台")
st.markdown("""
- 🍎 [coze](https://www.coze.cn/home)
- 🥭 [火山引擎](https://www.volcengine.com)
- 🍉 [飞书](https://www.feishu.cn)
- 🍊 [Dify](https://dify.ai)
- 🥝 [魔搭社区](https://modelscope.cn)
- 🫐 [Streamlit](https://streamlit.io)
- 🍏 [文心智能体平台](https://yiyan.baidu.com/agent)
- 🍌 [百宝箱](https://ai.baidu.com/creationtools)
- 🍐 [讯飞开放中心](https://www.xfyun.cn)
- 🥕 [Bolt.new](https://bolt.new)
- 🌶️ [Cursor](https://www.cursor.sh)
- 🥔 [Autodl](https://www.autodl.com)
""")

st.info("📌 点击网站名称即可跳转。")

