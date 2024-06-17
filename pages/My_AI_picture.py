import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():
    st.image("pages/pic_s/star.jpg", width=500)
    
    st.markdown(
        """
        ### 《摩羯座》
        - **项目获奖**: HiDream.ai首届AIGC创作大赛三等奖
        - **项目介绍**: 在2023年10月份我参加了HiDream.ai的千象创造营。此次HiDream.ai首届AIGC创作大赛有四个赛道，我选择了图片类的个人爱好赛道创作了《摩羯座》并获得三等奖。经过此次比赛的影响我在后面又将我的作品完善创作出一个完整系列的AIGC作品《12星座》，欢迎在下面的文章链接观看我完整的创作过程和全部图片作品。
        - **主要贡献**：主要负责人
        - **文章链接**: [《12星座》](https://juejin.cn/post/7300063447831117851)
        """
    )


if __name__ == "__main__":
    run()