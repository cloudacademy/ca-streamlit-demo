import streamlit as st

st.title("Streamlit Basics")
st.subheader("Markdown Editor")

with st.container(border=True):
    markdown, md_code = st.tabs(["Markdown Editor", "View code"])
    with markdown:

        md = st.text_area('Type in your markdown string (without outer quotes)')
    with st.container():
        st.divider()
        st.subheader("Rendered Markdown")
        st.markdown(md)

    with md_code:
        st.code("""
        md = st.text_area('Type in your markdown string (without outer quotes)')

        st.subheader("Rendered Markdown")
        st.markdown(md)
        """)

with st.expander("See code"):
        st.code("""
        md = st.text_area('Type in your markdown string (without outer quotes)')

        st.subheader("Rendered Markdown")
        st.markdown(md)
        """)
