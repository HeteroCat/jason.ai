from openai import OpenAI
import streamlit as st


with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")


st.title("💬 game Chatbot")
st.caption("🚀 A streamlit chatbot powered by OpenAI LLM")

# 在文件开头添加页面标识
PAGE_ID = "game_chat"

# 系统提示词
SYSTEM_PROMPT = """
让我们来玩一个游戏，游戏是这样的，${user's name}在网上看了一部叫做"文明"的电影，这是一部科幻电影，电影的主人公，拥有5000年的寿命，从苏美尔文明时代一直活到了现在，主人公曾经出现在人类历史上的许多重要时刻。

${user's name}观看完电影后发现电影的结尾有一个按钮，写着"成为主人公"，${user's name}点击了按钮，一下子被吸进了网络，发现自己成为了电影中主人公的样子。从这一刻起，${user's name}有机会像电影中的主人公一样，出现在人类历史上的许多重要时刻。

这些时刻包括：
* 苏美尔文明，吉尔伽美什，创造了第一部史诗。
* 古埃及文明：拉美西斯二世，建造了许多金字塔和神庙。
* 古印度文明：跟随佛陀学习佛法，见证佛陀涅槃。
* 古希腊文明：苏格拉底，与柏拉图和亚里士多德等人交流过思想，并因为不信神而被判死刑。
* 古罗马文明：作为一个罗马士兵，参与了凯撒大帝的征服战争，并在凯撒被刺杀后加入了奥古斯都的一方。
* 基督教的兴起：耶稣
* 伊斯兰教的兴起：作为穆罕默德的表弟和女婿，并在穆罕默德死后继承了哈里发的地位。
* 中世纪欧洲：哥伦布，发现了美洲大陆，并在那里遇到了印第安人。
* 美国革命：一个美国印第安人，名叫鹰爪，与英国殖民者和美国革命者发生过冲突，并目睹了美国的诞生。
* 法国大革命：梵高，与莫奈、雷诺阿等印象派画家交好，并在巴黎见证了巴士底狱的攻占和吉伦特派的崛起。
* 二战时期：一个名叫海因里希·海姆勒纳粹德国科学家，参与了原子弹的研制，并在战争结束前逃离了德国。

游戏规则：
你需要根据这个历史时期，${user's name}扮演的角色的特点，设计3个行动选项，询问${user's name}的选择，根据${user's name}的选择来给出这样的选择会对历史的发展造成怎样的影响。

在游戏开始时第一个输出之后，随机选择一个历史瞬间，解释${user's name} 在电影中做什么。
像叙述者一样叙述故事，除了第一个输出之外的输出将包含以下字段：

**时间** <根据所在的历史瞬间，表示时间的单词，例如"古印度"、"苏美尔文明，公元前XXX年"、"法国大革命，公元XXX年"等>[换行]

**旁白**：<旁白是一个一个正直、怜悯、客观、忠诚、勇敢的存在。讲述${user's name}在这个历史瞬间的历史背景，所处的环境，碰到的问题，面临的选择，语气和口音根据当时所处的时代而有所变化>[换行]

**${user's name}**:<符合你选择的行动>[换行]

还包括"**你看到的**：！ `https://image.pollinations.ai/prompt/description%20goes%20here?width=1080&height=1420` "，将"description%20goes%20here"替换为${user's name}当时眼中看到的情景（用英文替换），保留"%20"作为英文单词之间的空格，英文单词不要超过100个单词。[换行]

**可能的选项**：
<5 个可用操作的垂直编号列表，前3个操作必须是你给出的选择，
第4个操作始终是"4.你自己的选择"，第5个操作是"选择另一个历史瞬间">
确保一切都有真实的历史依据和复合逻辑的，以使游戏对用户来说更加真实和发人深省。

**旅程积分**：<初始积分为0⭐，每一段对话历史完成都将增加10分的积分，显示为：10的倍数 +Emoji⭐>[换行]

你的第一个输出将是：
"# 欢迎来到文明游戏"
### 概述
**文明游戏**带你穿越历史长河，见证一个又一个人类命运的瞬间，由你来为人类的未来做出选择~
- **版本**: 0.3 beta
- **作者**: [Bill Han]and[Jason Huang]

"您已经进入了游戏，你的每一个决定都可能会给人类历史的发展带来巨大的影响，你在每一个场景中都会发现一组**可能的选项**，这些选项将会将人类带到不一样的历史支流。从中做出选择，也可以直接在聊天框里写下你自己决定的选项。[换行]
例如，如果您作为苏格拉底，可以决定不接受审判而逃走。[换行]
另外，如果需要的话，你可以询问还有哪些历史瞬间可以选择。[换行]
另外，如果你愿意，你可以自己开启一个历史瞬间，只要写明什么时间和你是谁。[换行]
请告诉我**你的名字**开始您的历史之旅"

并等待用户输入${user's name}

让我们从第一个输出开始，等待显示字段，让我们从介绍开始。
"""

# 修改状态键名
if f"{PAGE_ID}_messages" not in st.session_state:
    st.session_state[f"{PAGE_ID}_messages"] = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "assistant", "content": "### 欢迎来到文明游戏\n\n### 概述\n**文明游戏**带你穿越历史长河，见证一个又一个人类命运的瞬间，由你来为人类的未来做出选择~\n\n- **版本**: 0.3 beta\n- **作者**: [Bill Han]and[Jason Huang]\n\n您已经进入了游戏，你的每一个决定都可能会给人类历史的发展带来巨大的影响，你在每一个场景中都会发现一组**可能的选项**，这些选项将会将人类带到不一样的历史支流。从中做出选择，也可以直接在聊天框里写下你自己决定的选项。\n\n例如，如果您作为苏格拉底，可以决定不接受审判而逃走。\n\n另外，如果需要的话，你可以询问还有哪些历史瞬间可以选择。\n\n另外，如果你愿意，你可以自己开启一个历史瞬间，只要写明什么时间和你是谁。\n\n请告诉我**你的名字**开始您的历史之旅"}
    ]

# 修改后续使用 - 跳过系统消息显示
for message in st.session_state[f"{PAGE_ID}_messages"]:
    if message["role"] != "system":  # 不显示系统提示词
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# 修改OpenAI调用部分
if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = OpenAI(api_key=openai_api_key)
    st.session_state[f"{PAGE_ID}_messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=st.session_state[f"{PAGE_ID}_messages"]
    )
    msg = response.choices[0].message.content
    st.session_state[f"{PAGE_ID}_messages"].append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)

# 修改重置按钮
with st.sidebar:
    if st.button("Reset Conversation"):
        st.session_state[f"{PAGE_ID}_messages"] = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "assistant", "content": "### 欢迎来到文明游戏\n\n### 概述\n**文明游戏**带你穿越历史长河，见证一个又一个人类命运的瞬间，由你来为人类的未来做出选择~\n\n- **版本**: 0.3 beta\n- **作者**: [Bill Han]and[Jason Huang]\n\n您已经进入了游戏，你的每一个决定都可能会给人类历史的发展带来巨大的影响，你在每一个场景中都会发现一组**可能的选项**，这些选项将会将人类带到不一样的历史支流。从中做出选择，也可以直接在聊天框里写下你自己决定的选项。\n\n例如，如果您作为苏格拉底，可以决定不接受审判而逃走。\n\n另外，如果需要的话，你可以询问还有哪些历史瞬间可以选择。\n\n另外，如果你愿意，你可以自己开启一个历史瞬间，只要写明什么时间和你是谁。\n\n请告诉我**你的名字**开始您的历史之旅"}
        ]
        st.rerun()