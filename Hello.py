# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="Jason's AI Fantasy World",
        page_icon="👋",
        layout="centered"
    )

    # 主页内容
    st.write("# Welcome to Jason's AI Fantasy World 👋")

    # 简介部分
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("my picture.jpg", width=200)  # 替换为你的头像链接

    with col2:
        st.markdown(
            """
            ### 我叫黄佩林，Jason.
            广东汕头人，22岁，来自广东财经大学，数学与应用数学专业
            - 《ChatGPT原理与应用开发》共创作者
            - 《Hugging llm》项目核心贡献者之一
            -   稀土掘金社区人气作者
            -   知名开源AI组织Datewhale意向成员
            -  AI音乐创作者



            欢迎访问我的博客[Hetero Cat](https://juejin.cn/user/2221479480010573)和音乐[HeteroCat401](https://www.douyin.com/user/self)
            """
        )
# 项目部分
    st.write("## 研究方向")
    st.markdown(
        """
       我的研究兴趣在于大语言模型与各行各业的结合应用，运用大语言模型创作不可思议的作品。 我目前是在深圳跳舞兰科技公司从事AI工作。 
       
       我的研究重点是大型语言模型，如基于LLM的代理、基于LLM API的应用开发、基于LLM的行业经济创新等。大型语言模型是我未来的研究方向。 我对 LLM 有着浓厚的兴趣， 提示prompt工程、优化策略、Agent智能体、应用程序开发以及与 LLM 相关的其他方面。 我一直积极参与各种与LLM相关的开源项目，并获得了一些经验。
        """
    )
    # 项目部分
    st.write("## 项目经历")
    st.markdown(
        """
        ### Project 1
        - **Description**: Description of project 1...
        - **Technologies**: Python, Streamlit, etc.
        - **Link**: [GitHub](https://github.com/your-repo/project-1)
        
        ### Project 2
        - **Description**: Description of project 2...
        - **Technologies**: Python, Streamlit, etc.
        - **Link**: [GitHub](https://github.com/your-repo/project-2)
        """
    )
    # 工作部分
    st.write("## 工作经历")
    st.markdown(
        """
        ### Project 1
        - **Description**: Description of project 1...
        - **Technologies**: Python, Streamlit, etc.
        - **Link**: [GitHub](https://github.com/your-repo/project-1)
        
        ### Project 2
        - **Description**: Description of project 2...
        - **Technologies**: Python, Streamlit, etc.
        - **Link**: [GitHub](https://github.com/your-repo/project-2)
        """
    )
    # 技能部分
    st.write("## 技能")
    st.markdown(
        """
        - **编程语言**: Python,C,R,Matlab
        - **框架和库**: Openai,NumPy,Pandas,Matplotlib,Streamlit,Flash, PyTorch 等等.
        - **工具**: ChatGPT,文心一言,Midjourney,Suno,Sora,coze,FineBI 等等.
        """
    )

    # 联系方式部分
    st.write("## 联系方式")
    st.markdown(
        """
        - **Email**: 1580823387@qq.com
        - **LinkedIn**: [MY LinkedIn](https://www.linkedin.com/in/your-profile)
        - **GitHub**: [HeteroCat](https://github.com/HeteroCat)
        """
    )
   

if __name__ == "__main__":
    run()
