import streamlit as st

st.write("## 智能体商店")
col1, col2, col3 = st.columns(3)  # 在每一列中展示一张图片
with col1:
    st.image("pages/pic_s/图片 1.png", width=200)  # 替换为您的图片链接
    st.markdown("[韩语老师Lisa](https://bailian.console.aliyun.com/share/22c3b24cce1f4bb18e2de7db31846031?memoryId=f9bbf2a9f1af4058bc35b46f5b83b2b0)")

with col2:
    st.image("pages/pic_s/图片 2.png", width=200)  # 替换为您的图片链接
    st.markdown("[AI鲜花画布](https://www.coze.cn/store/project/7487864472749490202?from=store_search_suggestion&bid=6gtge610c8g1b)")

with col3:
    st.image("pages/pic_s/图片 3.png", width=200)  # 替换为您的图片链接
    st.markdown("[AI音乐超级创作台](https://www.coze.cn/store/project/7458678213078777893?bid=6gtgec9ac1009)")