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
    "<h3>Project 1: AFrosty Chatbot 🤖</h3>"
    "<p>\
        <b>Description 📝 :</b>\
        The primary purpose of the AFrosty Chatbot project is to provide an\
        intuitive and efficient way for users to interact with and query\
        Snowflake and PostgreSQL databases. This solution leverages Natural\
        Language input from users to generate and execute SQL queries based\
        on their configuration details\
    </p>"
    "<p>\
        <b>Technologies Used 💻:</b>\
        Python, Streamlit, Postgresql, Snowflake,\
        Openai, Psycopg2, Snowflake connector, Docker, Geeklab\
    </p>"
    "<p><b>GitHub Repository 🚀:</b> "
    '<a href=\
    "https://geeklab.afourtech.com/snowflakeaccel/llm_chatbot/-/tree/development">\
    Link to Geeklab</a></p>'
    "</div>",
    unsafe_allow_html=True,
)

st.markdown(
    f'<div style="{project_card_style}">'
    "<h3>Project 2: My Portfolio 📁</h3>"
    "<p>\
        <b>Description 📝:</b>\
        This portfolio project is built with Streamlit. With this portfolio, I\
        aim to provide a glimpse of my professional journey, including my\
        educational background, work experience, skills, and various projects.\
    </p>"
    "<p>\
        <b>Technologies Used 💻:</b>\
        Streamlit, HTML, CSS\
    </p>"
    "<p><b>GitHub Repository 🚀:</b> "
    '<a href=\
    "https://github.com/M74-dot/manisha-portfolio">\
    Link to Github</a></p>'
    "</div>",
    unsafe_allow_html=True,
)

st.markdown(
    f'<div style="{project_card_style}">'
    "<h3>Project 3: Online Yoga Trainer 🧘</h3>"
    "<p>\
        <b>Description 📝:</b>\
        This portfolio project is built with StreamlitWith this portfolio, I\
        aim to provide a glimpse of mynm professional journey, including my\
        educational background, work experience, skills, and various projects.\
    </p>"
    "<p>\
        <b>Technologies Used 💻:</b>\
        Meadiapipe, Streamlit, HTML, CSS\
    </p>"
    "<p><b>GitHub Repository 🚀:</b> "
    '<a href=\
    "https://geeklab.afourtech.com/snowflakeaccel/llm_chatbot/-/tree/development">\
    Link to Github</a></p>'
    "</div>",
    unsafe_allow_html=True,
)

st.markdown(
    f'<div style="{project_card_style}">'
    "<h3>Project 4: TODO App ✅</h3>"
    "<p>\
        <b>Description 📝:</b>\
        In my 'Todo App' project, I developed a web application using Python\
        and Flask that allows users to manage their tasks efficiently.\
        Leveraging REST API principles, I enabled seamless interaction with\
        the app and employed SQLAlchemy for database management. Postman was\
        utilized for testing and validation, resulting in a user-friendly task\
        management solution.\
    </p>"
    "<p>\
        <b>Technologies Used 💻:</b>\
        python, flask, rest api, sqlalchemy, postman \
    </p>"
    "<p><b>GitHub Repository 🚀:</b> "
    '<a href=\
    "https://github.com/M74-dot/todo-api">\
    Link to Github</a></p>'
    "</div>",
    unsafe_allow_html=True,
)

st.markdown(
    f'<div style="{project_card_style}">'
    "<h3>Project 5: Toxic Comments Remover 🚫</h3>"
    "<p>\
        <b>Description 📝:</b>\
        My 'Toxic Comments Remover for YouTube' project, built with Python\
        and Django, offers YouTube content creators a powerful tool to filter\
        and eliminate toxic comments from their videos. Through a\
        user-friendly web interface crafted with HTML and CSS, users can\
        easily manage and moderate their comments section, fostering a safer\
        and more positive online community.\
    </p>"
    "<p>\
        <b>Technologies Used 💻:</b>\
        python, django, HTML, CSS, Youtube API's \
    </p>"
    "<p><b>GitHub Repository 🚀:</b> "
    '<a href=\
    "https://github.com/M74-dot/Toxic_comments_remover">\
    Link to Github</a></p>'
    "</div>",
    unsafe_allow_html=True,
)
