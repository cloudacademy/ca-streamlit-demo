import streamlit as st
import pandas as pd
import random

st.set_page_config(layout="wide")

st.title("Streamlit Basics")

with st.container(border=True):
    text, data, chat, markdown = st.tabs(["Text", "Data", "Chat", "Markdown Editor"])

    with text:
        st.title("Titles")
        st.divider()
        st.header("Headers")
        st.subheader("Subheaders")
        st.text("Normal text")
        st.markdown("***Markdown Text***")
        st.code("for i in range(8): print(i)")

        with st.expander("See code"):
            st.code("""
            st.title("Titles")
            st.divider()
            st.header("Headers")
            st.subheader("Subheaders")
            st.text("Normal text")
            st.markdown("***Markdown Text***")
            st.code("for i in range(8): print(i)")
            """)

    with data:
        st.subheader("Display data using a data frame")
        df = pd.DataFrame(
            {
                "name": ["Spirited Away", "Princess Mononoke", "My Neighbor Totoro"],
                "url": ["https://m.imdb.com/title/tt0245429/", "https://m.imdb.com/title/tt0119698/", "https://m.imdb.com/title/tt0096283/"],
                "reviews": [random.randint(0, 1000) for _ in range(3)],
                "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
            }
        )
        st.dataframe(
            df,
            column_config={
                "name": "Title",
                "reviews": st.column_config.NumberColumn(
                    "Reviews",
                    help="Total number of reviews",
                    format="%d ⭐",
                ),
                "url": st.column_config.LinkColumn("IMDb page"),
                "views_history": st.column_config.LineChartColumn(
                    "Views (past 30 days)", y_min=0, y_max=5000
                ),
            },
            hide_index=True,
        )

        with st.expander("See code"):
            st.code("""
            df = pd.DataFrame(
                {
                    "name": ["Spirited Away", "Princess Mononoke", "My Neighbor Totoro"],
                    "url": ["https://m.imdb.com/title/tt0245429/", "https://m.imdb.com/title/tt0119698/", "https://m.imdb.com/title/tt0096283/"],
                    "reviews": [random.randint(0, 1000) for _ in range(3)],
                    "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
                }
            )
            st.dataframe(
                df,
                column_config={
                    "name": "Title",
                    "reviews": st.column_config.NumberColumn(
                        "Reviews",
                        help="Total number of reviews",
                        format="%d ⭐",
                    ),
                    "url": st.column_config.LinkColumn("IMDb page"),
                    "views_history": st.column_config.LineChartColumn(
                        "Views (past 30 days)", y_min=0, y_max=5000
                    ),
                },
                hide_index=True,
            )
            """)
    
    with chat:
        st.subheader("Enter in a prompt to the chat")
        prompt = st.chat_input("Say something")
        if prompt:
            st.write(f"You entered the following prompt: :blue[{prompt}]")

        with st.expander("See code"):
            st.code("""
            prompt = st.chat_input("Say something")
            if prompt:
                st.write(f"You entered the following prompt: :blue[{prompt}]")
            """)

    with markdown:
        st.subheader("Edit and render Markdown")
        md = st.text_area('Type in your markdown string (without outer quotes)')
        with st.container():
            st.divider()
            st.subheader("Rendered Markdown")
            st.markdown(md)
        
        with st.expander("See code"):
            st.code("""
            md = st.text_area('Type in your markdown string (without outer quotes)')

            st.subheader("Rendered Markdown")
            st.markdown(md)
            """)


