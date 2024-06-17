import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():
    st.image("pages/pic_s/HCsuno.png", width=600)
    
    st.markdown(
        """
        ### DY : HeteroCat401
        - **项目成果**: 歌曲《missing》登上suno.ai趋势榜，获得17w+播放量和近1k点赞量。
        - **项目介绍**: 《missing》这首歌是我在试用完suno平台后，将自己几年前写的歌词放进去生成的AI音乐作品，当时心血来潮写的歌词没想到在suno平台真正变成了一首动人的音乐。而且被这么多人喜欢感觉非常奇妙，以后会在suno持续创作新的音乐，下面是我的suno主页和抖音主页欢迎大家关注我━(*｀∀´*)ノ亻!
        - **主要贡献**：主理人
        - **主页链接**: [Suno：HeteroCat401](https://suno.com/@heterocat401)      [抖音：HeteroCat401](https://www.douyin.com/user/self)
        """
    )

if __name__ == "__main__":
    run()