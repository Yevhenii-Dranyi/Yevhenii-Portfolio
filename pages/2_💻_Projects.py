import streamlit as st


st.set_page_config(
    page_title="Projects",
    page_icon="💼",
    layout="wide",
)

st.title("💼 Projects")
st.write("Here are some of the projects I've worked on:")

project_card_style = (
    "background-color: #f0f0f0;\
    margin-top: 20px;\
    padding: 20px;\
    border-radius: 15px;"
)

st.markdown(
    f'<div style="{project_card_style}">'
    "<h3>Project 1: AFrosty Chatbot</h3>"
    "<p>\
        <b>Description:</b>\
        The primary purpose of the AFrosty Chatbot project is to provide an\
        intuitive and efficient way for users to interact with and query\
        Snowflake and PostgreSQL databases. This solution leverages Natural\
        Language input from users to generate and execute SQL queries based\
        on their configuration details\
    </p>"
    "<p>\
        <b>Technologies Used:</b>\
        Python, Streamlit, Postgresql, Snowflake,\
        Openai, Psycopg2, Snowflake connector, Docker, Geeklab\
    </p>"
    "<p><b>GitHub Repository:</b> "
    '<a href=\
    "https://geeklab.afourtech.com/snowflakeaccel/llm_chatbot/-/tree/development">\
    Link to Geeklab</a></p>'
    "</div>",
    unsafe_allow_html=True,
)

st.markdown(
    f'<div style="{project_card_style}">'
    "<h3>Project 2: My Portfolio</h3>"
    "<p>\
        <b>Description:</b>\
        This portfolio project is built with Streamlit. With this portfolio, I\
        aim to provide a glimpse of my professional journey, including my\
        educational background, work experience, skills, and various projects.\
    </p>"
    "<p>\
        <b>Technologies Used:</b>\
        Streamlit, HTML, CSS\
    </p>"
    "<p><b>GitHub Repository:</b> "
    '<a href=\
    "https://github.com/M74-dot/manisha-portfolio">\
    Link to Github</a></p>'
    "</div>",
    unsafe_allow_html=True,
)

st.markdown(
    f'<div style="{project_card_style}">'
    "<h3>Project 3: Online Yoga Trainer</h3>"
    "<p>\
        <b>Description:</b>\
        This portfolio project is built with StreamlitWith this portfolio, I\
        aim to provide a glimpse of mynm professional journey, including my\
        educational background, work experience, skills, and various projects.\
    </p>"
    "<p>\
        <b>Technologies Used:</b>\
        Streamlit, HTML, CSS\
    </p>"
    "<p><b>GitHub Repository:</b> "
    '<a href=\
    "https://geeklab.afourtech.com/snowflakeaccel/llm_chatbot/-/tree/development">\
    Link to Github</a></p>'
    "</div>",
    unsafe_allow_html=True,
)