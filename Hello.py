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
    st.write("# Welcome to Jason's AI World 👋")

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
       我的研究兴趣在于大语言模型与各行各业的结合应用，运用大语言模型创作不可思议的作品。 我目前是在深圳某科技公司从事AI工作。 
       
       我的研究重点是大型语言模型，如基于LLM的代理、基于LLM API的应用开发、基于LLM的行业或者公司业务的智能升级优化等。大型语言模型是我未来的研究方向。 我对 LLM 有着浓厚的兴趣， 提示prompt工程、优化策略、Agent智能体、应用程序开发以及与多模态相关的其他方面。 我一直积极参与各种与LLM相关的开源项目，并获得了一些经验。
        """
    )
    # 项目部分
    st.write("## 项目经历")
    st.image("hugging llm 001.png", width=800)
    
    st.markdown(
        """
        ### 《Hugging llm》
        - **项目背景**: 随着ChatGPT的爆火，其背后其实蕴含着一个基本事实：AI能力得到了极大突破——大模型的能力有目共睹，未来只会变得更强。这世界唯一不变的就是变，适应变化、拥抱变化、喜欢变化，天行健君子以自强不息。我们相信未来会有越来越多的大模型出现，AI正在逐渐平民化，将来每个人都可以利用大模型轻松地做出自己的AI产品。所以，我们把项目起名为HuggingLLM，我们相信我们正在经历一个伟大的时代，我们相信这是一个值得每个人全身心拥抱的时代，我们更加相信这个世界必将会因此而变得更加美好。
        - **项目介绍**: 该项目主要介绍 ChatGPT 原理、使用和应用，降低使用门槛，让更多感兴趣的非NLP或算法专业人士能够无障碍使用LLM创造价值。ChatGPT改变了NLP行业，甚至正在改变整个产业。我们想借这个项目将ChatGPT介绍给更多的人，尤其是对此感兴趣、想利用相关技术做一些新产品或应用的学习者，尤其是非本专业人员。希望新的技术突破能够更多地改善我们所处的世界。
        - **主要贡献**：我主要负责第八章ChatGPT的商业应用-LLM是星辰大海，介绍了ChatGPT的背景，以及其在：搜索、办公、教育、游戏、音乐、零售电商、广告营销、媒体新闻、金融、医疗、设计、影视、工业这些方面的商业实践案例，为开发者提供商业思路。
        - **项目链接**: [GitHub](https://github.com/datawhalechina/hugging-llm)
        - **实体书**：目前该项目已经由人民邮电出版社出版为《ChatGPT原理与应用开发》,购买[链接](https://u.jd.com/ficxj2d)
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
  


    # 嵌入自定义CSS样式
    st.markdown(
        """
        <style>
        .progress {
            width: 100%;
            background-color: #e0e0e0;
            border: 2px solid #000000; /* 边框颜色和宽度 */
            border-radius: 5px;
            overflow: hidden;
            height: 30px;
        }
        .progress-bar {
            height: 100%;
            text-align: right;
            padding: 0 10px;
            color: white;
            border-radius: 5px 0 0 5px;
        }
        </style>
        """,
             unsafe_allow_html=True
        )

    def progress_bar(proficiency):
            color = "#007bff"
            return f"""
                <div class="progress">
                    <div class="progress-bar" style="width: {proficiency}%; background-color: {color};">{proficiency}%</div>
                </div>
            """

        # 标题部分
    st.write("## 技能")

        # 编程语言
    st.markdown("### 编程语言")
    languages = {
            "Prompt": 100,
            "Python": 80,
            "Matlab": 70,
            "C": 65,
            "R": 65,
            
        }

    cols = st.columns(len(languages))
    for (language, proficiency), col in zip(languages.items(), cols):
            col.markdown(f"**{language}**")
            col.markdown(progress_bar(proficiency), unsafe_allow_html=True)

        # 框架和库
    st.markdown("### 框架和库")
    frameworks = {
            "Matplotlib": 85,
            "Pandas": 80,
            "Openai": 80,
            "NumPy": 65,
            "Streamlit": 60,
            "Flash": 60,
            "PyTorch": 50
        }

    cols = st.columns(len(frameworks))
    for (framework, proficiency), col in zip(frameworks.items(), cols):
            col.markdown(f"**{framework}**")
            col.markdown(progress_bar(proficiency), unsafe_allow_html=True)

        # 工具
    st.markdown("### 工具")
    tools = {
            "ChatGPT": 90,
            "文心一言": 90,
            "coze": 75,
            "Suno": 70,
            "Midjourney": 60,
            "Sora": 60
        }

    cols = st.columns(len(tools))
    for (tool, proficiency), col in zip(tools.items(), cols):
            col.markdown(f"**{tool}**")
            col.markdown(progress_bar(proficiency), unsafe_allow_html=True)
    # 联系方式部分
    st.write("## 联系方式")
    st.markdown(
        """
        - **Email**: 1580823387@qq.com
        - **LinkedIn**: [MY LinkedIn](https://www.linkedin.com/in/%E4%BD%A9%E6%9E%97-%E9%BB%84-6650b4264/)
        - **GitHub**: [HeteroCat](https://github.com/HeteroCat)
        """
    )
   

if __name__ == "__main__":
    run()
