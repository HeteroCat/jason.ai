
import streamlit as st
import pandas as pd
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
            广东汕头人，24岁，毕业于广东财经大学，数学与应用数学专业
            - 《ChatGPT原理与应用开发》共创作者
            - 《Hello-Agents》项目核心贡献者(Trending TOP1)
            -   AI开源组织Datewhale成员、助教、优秀学习者
            -   上海交通大学AI访谈嘉宾
            -   稀土掘金社区AI人气作者
            -  职业：Agent开发工程师
            


            欢迎访问我的博客[Hetero Cat](https://juejin.cn/user/2221479480010573)

            也欢迎试玩左侧边栏的AI Demo，更多Demo在开发中。
            """
        )
        
# 项目部分
    st.write("## 研究方向")
    st.markdown(
        """
       我的研究兴趣在于大语言模型与各行各业的结合应用，运用大语言模型创作不可思议的作品。 我目前是在深圳探知未来科技公司从事AI工作。 
       
       我的研究重点是大型语言模型与智能体，如基于LLM的代理、基于LLM API的应用开发、基于LLM的行业或者公司业务的智能升级优化等。大型语言模型与智能体是我未来的研究方向。 我对 LLM 有着浓厚的兴趣， prompt工程、数据可视化、Agent智能体、应用程序开发以及与多模态相关等方面。 我一直积极参与各种与LLM相关的开源项目，并获得了一些经验。
        """
    )
    # 项目部分
    st.write("## 项目经历")

    st.image("hello-agents.png", width=700)
    
    st.markdown(
        """
        ### 《Hello-Agents》
        - **项目背景**: 如果说 2024 年是"百模大战"的元年，那么 2025/26 年无疑开启了"Agent 元年"。技术的焦点正从训练更大的基础模型，转向构建更聪明的智能体应用。为此，我们发起了 Hello-Agents 项目，希望能为大家提供一份从零开始、理论与实战并重的智能体系统构建指南。
        - **项目介绍**: 如今 Agent 构建主要分为两派，一派是 Dify，Coze，n8n 这类软件工程类 Agent，其本质是流程驱动的软件开发，LLM 作为数据处理的后端；另一派则是 AI 原生的 Agent，即真正以 AI 驱动的 Agent。本教程旨在带领大家深入理解并构建——真正的全面的 AI Agent。我们相信，最好的学习方式就是动手实践。希望学习者能够从一名大语言模型的"使用者"，蜕变为一名智能体系统的"构建者"。
        - **主要贡献**：我主要负责撰写第五章内容，涵盖扣子（Coze）智能体和 Dify 智能体的搭建实践。从页面介绍到模型选择，从开发流程讲解到提示词和配置示范，完整的介绍了一整套当前主流的低代码平台智能体开发范式。以及vide-coding了一个方便国内网络服务的教程Cookbook网站
        - **项目链接**: [《Hello-Agents》](https://github.com/datawhalechina/hello-agents) [《Cookbook》](https://book.heterocat.com.cn)
        """
    )

    st.image("hugging llm 001.png", width=700)
    
    st.markdown(
        """
        ### 《Hugging llm》
        - **项目背景**: 随着ChatGPT的爆火，其背后其实蕴含着一个基本事实：AI能力得到了极大突破——大模型的能力有目共睹，未来只会变得更强。这世界唯一不变的就是变，适应变化、拥抱变化、喜欢变化，天行健君子以自强不息。我们相信未来会有越来越多的大模型出现，AI正在逐渐平民化，将来每个人都可以利用大模型轻松地做出自己的AI产品。所以，我们把项目起名为HuggingLLM，我们相信我们正在经历一个伟大的时代，我们相信这是一个值得每个人全身心拥抱的时代，我们更加相信这个世界必将会因此而变得更加美好。
        - **项目介绍**: 该项目主要介绍 ChatGPT 原理、使用和应用，降低使用门槛，让更多感兴趣的非NLP或算法专业人士能够无障碍使用LLM创造价值。ChatGPT改变了NLP行业，甚至正在改变整个产业。我们想借这个项目将ChatGPT介绍给更多的人，尤其是对此感兴趣、想利用相关技术做一些新产品或应用的学习者，尤其是非本专业人员。希望新的技术突破能够更多地改善我们所处的世界。
        - **主要贡献**：我主要负责第八章ChatGPT的商业应用-LLM是星辰大海，介绍了ChatGPT的背景，以及其在：搜索、办公、教育、游戏、音乐、零售电商、广告营销、媒体新闻、金融、医疗、设计、影视、工业这些方面的商业实践案例，为开发者提供商业思路。
        - **项目链接**: [《Hugging llm》](https://github.com/datawhalechina/hugging-llm)
        - **实体书**：目前该项目已经由人民邮电出版社出版为《ChatGPT原理与应用开发》,购买[链接](https://u.jd.com/ficxj2d)
        """
    )
    
    st.image("AsyncTrader.png", width=700)
    
    st.markdown(
        """
        ### 《AsyncTrader》
        - **项目获奖**: 2023年百度大模型应用创新挑战赛-最佳创意作品奖
        - **项目介绍**: 使用 ChatGPT 自动运行量化交易系统听起来很酷，不是吗？使用AGI（通用人工智能）构建一个完整的量化交易系统仍然相当具有挑战性。然而，幸运的是，通过大语言模型似乎有一种可行的方法来使用现有的成熟量化交易系统，我们正在研究它。借助langchain的控制流程，我们使用ChatGPT自动编写和回测量化交易策略，并提供文档问答功能。目前，Freqtrade定量系统已经实现了相当全面的工作流程。此外，它还支持中国的 AkShare 和 Vnpy 的部分功能。​
        - **主要贡献**：我主要负责数字模型优化以及系统流程优化。
        - **项目链接**: [《AsyncTrader》](https://github.com/HeteroCat/AsyncTrader)
        """
    )

    st.image("juejin2026.png", width=700)
    
    st.markdown(
        """
        ### 《HeteroCat》
        - **项目获奖**: 2023年度稀土掘金人气作者
        - **项目介绍**: 从2022年7月份开始，我在稀土掘金社区做人工智能相关的学习分享和数据分析，数据挖掘相关的技术博客，目前累加阅读量 6w+, 其中文章《我眼中的 ChatGPT》曾获得全站第三的热度，《AI 爆发的一年 2023 总结》在掘金 2023 年度技术盘点征文获奖，同时加入掘金社区人工智能创作者扶持计划。并获得 2023 年掘金社区年度人气作者。
        - **代表文章**： 
        - [《AI 爆发的一年 2023 总结》](https://juejin.cn/post/7317908960756662306)
        - [《一些更丰富的prompt技巧--from GitHub》](https://juejin.cn/post/7283426137968525312)
        - [《我眼中的chatGPT》](https://juejin.cn/post/7198426159478669373)
        - **博客链接**: [HeteroCat](https://juejin.cn/user/2221479480010573)
        """
    )
    st.image("dw_life.png", width=700)
    
    st.markdown(
        """
        ### 《Datawhale》
        - **组织介绍**: Datawhale 是一个专注于数据科学与 AI 领域的开源组织，从2023年初与Datawhale结识从此开始了我真正的AI学习实践的旅程，从懵懵懂懂的AI爱好者，到动手去实践一个个AI模型代码实现，再到参与大模型开源项目，并且最后幸运地出版成一本书。每一步都是如此奇妙，感谢datawhale。一路走来在 datawhale 里我不但收获了知识，还认识了很多优秀的朋友增长了见识，同时也让我认识到自己的不足和差距，向他们学习看齐，成为催促我前进的动力。最近 datawhale 在 GitHub 上进入全球前100名，在这里也祝愿 datawhale 越来越好，欢迎大家加入。
        - **组织收获**: 目前是Datawhale的意向成员、优秀学习者、助教
        - **参与活动**：《动手学数据分析》、《动手学深度学习》、《动手学AI视频生成》等等
        - **组织贡献**： 
        - [《hugging llm》](https://github.com/datawhalechina/hugging-llm)
        - [《hello-agents》](https://github.com/datawhalechina/hello-agents)
        - [《黄佩林的AI成长之路》](https://mp.weixin.qq.com/s/Lj_Wje3B4CkpH6SQT8fd1Q)
        
        
        - **开源链接**: [Datawhale](https://github.com/datawhalechina)
        """
    )
    st.write("## 证书")
    col3, col4, col5 = st.columns(3)  # 在每一列中展示一张图片
    with col3:
        st.image("Certificate/1.png", width=200)  # 替换为您的图片链接
        st.markdown("亚马逊云科技生成式AI精英证书")

    with col4:
        st.image("Certificate/2.png", width=200)  # 替换为您的图片链接
        st.markdown("范德堡大学prompt课程证书")

    with col5:
        st.image("Certificate/3.png", width=200)  # 替换为您的图片链接
        st.markdown("百度大模型应用创新挑战赛证书")

    col6, col7, col8 = st.columns(3)  # 在每一列中展示一张图片
    with col6:
        st.image("Certificate/4.png", width=200)  # 替换为您的图片链接
        st.markdown("科大讯飞prompt证书")

    with col7:
        st.image("Certificate/5.png", width=200)  # 替换为您的图片链接
        st.markdown("百度prompt证书")

    with col8:
        st.image("Certificate/12.jpg", width=200)  # 替换为您的图片链接
        st.markdown("百度智能体平台开发者证书")
    col9, col10, col11 = st.columns(3)  # 在每一列中展示一张图片
    with col9:
        st.image("Certificate/7.jpg", width=200)  # 替换为您的图片链接
        st.markdown("魔搭社区AI智能体工程师证书")

    with col10:
        st.image("Certificate/8.jpg", width=200)  # 替换为您的图片链接
        st.markdown("可灵Lora微调结业证书")

    with col11:
        st.image("Certificate/9.jpg", width=200)  # 替换为您的图片链接
        st.markdown("AI视频获奖证书")
    col12, col13, col14 = st.columns(3)  # 在每一列中展示一张图片
    with col12:
        st.image("Certificate/FT.jpg", width=200)  # 替换为您的图片链接
        st.markdown("讯飞Fine-tuning微调证书")

    with col13:
        st.image("Certificate/AIcoding.jpg", width=200)  # 替换为您的图片链接
        st.markdown("豆包AI coding证书")

    with col14:
        st.image("Certificate/yindao.jpg", width=200)  # 替换为您的图片链接
        st.markdown("影刀AI power证书")

    # 工作部分
    st.write("## 工作经历")
    st.markdown(
        """
        ### 深圳市华云科技研发有限公司--         Agent开发工程师
        - **Time**：2025.08-至今
        - **Description**: 根据公司业务开发智能AI问数，AI写作，AI数据分析，AI自动化和AI批改等agent智能体。
        - **Technologies**: 工作流智能体开发(FastGPT/扣子/Dify/N8N)，skills Agents技能开发, 数据后台开发
        """
    )
    st.markdown("项目一：科研论文写作skills开发")
    st.markdown(
        """
        - **Description**: 
            - 1.基于Claude Code开发科研论文写作的AI辅助技能，构建结构化写作流程的skill体系，包括文献检索、大纲描述、数据分析等模块的智能生成与润色。
            - 2.设计并优化学术论文的格式化输出模板，支持多种期刊格式的自动适配与引用管理，提升科研人员的写作效率与规范性。
            - 3.搭建用户反馈收集系统，持续迭代模型输出质量，建立论文写作的知识库与最佳实践案例库。
        - **Technologies**: Agentic Engineering, Prompt, Python, Claude code, 学术写作规范
        """
    )

    st.markdown("项目二：LlamaFactory大模型微调课程")
    st.markdown(
        """
        - **Description**: 
            - 1.基于LlamaFactory框架开发面向技术人员的大模型微调实战课程，涵盖LoRA、QLoRA、全参数微调等技术的原理讲解与代码实践。
            - 2.设计Claude Code指令集操作llama factory进行大模型微调，包括数据预处理、模型训练、效果评估与部署上线的完整Pipeline。
            - 3.编写并录制了课程配套的完整文档与视频教程，支持学员在线完成模型微调与效果实验。
        - **Technologies**: LlamaFactory, LoRA/QLoRA, PyTorch, Claude code, 华为昇腾, 数据治理
        """
    )

    st.markdown("项目三：智能问数智能体")
    st.markdown(
        """
        - **Description**: 
            - 1.开发基于自然语言交互的数据查询和可视化分析智能体，支持用户通过对话方式完成复杂数据分析和报表生成。
            - 2.构建数据库表结构调用理解工作流模块，实现自动的表关系识别、字段语义匹配与SQL语句生成优化。
            - 3.集成MCP进行数据可视化，多轮对话上下文管理，支持追问、澄清与可视化图表生成，降低非技术人员的数据获取门槛。
        - **Technologies**: MYSQL, FastGPT/Dify, MCP, 数据可视化, RAG
        """
    )

    st.markdown("项目四：智能批改智能体")
    st.markdown(
        """
        - **Description**: 
            - 1.开发面向教育场景的作业智能批改系统，实现自动评分、错误标注、改进建议生成与知识点总结分析建议。
            - 2.构建多维度评估体系（内容完整性、逻辑结构、语言表达、格式规范），支持主观题的语义理解与个性化反馈。
            - 3.设计教师审核与人工修正工作流，通过人机协同持续优化批改模型的准确率与反馈质量。
        - **Technologies**:  Prompt chain, RAG知识库, OCR, FastGPT
        """
    )   
    st.markdown(
        """
        ### 深圳跳舞兰科技有限公司--         AI工程师
        - **Time**：2024.06-2025.07
        - **Description**: 根据公司业务开发智能AI客服，AI画布，AI数据分析，AI自动化和AI营销等agent智能体。
        - **Technologies**: 智能体开发(扣子/dify)，小程序AI开发, 数据后台开发
        """
    )
    st.markdown("项目一：[业务AI化系统](http://ai.xiangbinmeigui.com/)")
    data = pd.DataFrame({
        '内容': ['六项具体业务相关内容'],
        '原来所需时间': ["12h"],
        '优化后时间': ['1.2h'],
        '提升效率': ['约90%']
    })

    st.dataframe(data)
    st.markdown("项目二：[花美家AI](http://huameijia.com.cn/)")
    st.video("https://www.youtube.com/watch?v=2xcdmlqJjMM")
    st.markdown("项目三：[AI画布](https://www.coze.cn/store/project/7487864472749490202)")
    st.image("AIhuabu.png", width=700)
    
    st.markdown(
        """
        ### 广州普瑞纯证医疗科技有限公司 --  提示词工程师（实习）
        - **Time**：2023.06-2024.06
        - **Description**: 
             - 1.医疗专业文本生成AI产品的提示词进行具体细节的优化和补充扩充 2.0 版本，并协助 AI 产品经理进行公司新的 AIGC产品测试。进行 AI 大模型方面的探索，赋能公司的医疗 AIGC 产品。
             - 2.后端接口开发:承担了公司一部分邮件推送系统和订阅系统的接口开发。
             - 3.数据治理主要负责将国民经济行业分类和国标专利 IPC 这两个表进行匹配，包括通过 Python 代码进行数据清洗和整合、数据分析最后通过模糊算法进行匹配。
        - **Technologies**: Python，正则表达式，prompt 工程开发，产品测试，flask开发
        
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
            "Prompt": 95,
            "Python": 90,
            "Matlab": 70,
            "JS/TS": 65,
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
            "Openai": 70,
            "Langchain": 65,
            "FastAPI": 65,
            "Flask": 60,
            "PyTorch": 50
        }

    cols = st.columns(len(frameworks))
    for (framework, proficiency), col in zip(frameworks.items(), cols):
            col.markdown(f"**{framework}**")
            col.markdown(progress_bar(proficiency), unsafe_allow_html=True)

        # 工具
    st.markdown("### 工具")
    tools = {
            "Claude code": 90,
            "Trae": 90,
            "Coze": 85,
            "Dify": 70,
            "即梦":65,
            "可灵": 60
           
        }

    cols = st.columns(len(tools))
    for (tool, proficiency), col in zip(tools.items(), cols):
            col.markdown(f"**{tool}**")
            col.markdown(progress_bar(proficiency), unsafe_allow_html=True)
    # 联系方式部分
    st.write("## 联系 方式")
    st.markdown(
        """
        - **phone**: 19830512935
        - **Email**: 1580823387@qq.com
        - **Douyin**: [Butterstorm](https://www.douyin.com/user/MS4wLjABAAAAvBkZt534BdaLk_KUZpdWBa3CzGgL-nvlMNZKWHD054U?previous_page=app_code_link)
        - **GitHub**: [HeteroCat](https://github.com/HeteroCat)
        """
    )
   

if __name__ == "__main__":
    run()
