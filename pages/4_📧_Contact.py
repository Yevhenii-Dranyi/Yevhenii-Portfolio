import streamlit as st


st.set_page_config(
    page_title="Let's Connect",
    page_icon="✉️",
    layout="wide",
)

custom_css = """
<style>
    .bullet-point {
        margin-left: 20px;
        padding-left: 10px;
        position: relative;
    }
</style>
"""

st.subheader("🚀 Let's connect")

st.markdown("""
<div style="background-color: #f0f0f0; padding: 40px; text-align: center;
border-radius: 15px;">
    <h1 style="color: #333; font-size: 24px; font-weight:bold;">
        Feel free to get in touch with me:
    </h1>
    <a href="mailto:malimanisha1525@gmail.com" style="text-decoration: none;\
        font-size:20px">📧 Email</a>
    <a href="https://www.linkedin.com/in/manisha-mali-3b5243207/"\
        style="text-decoration: none; font-size:20px">🔗 LinkedIn</a>
    <a href="https://www.instagram.com/manisha_m.a.l.i"\
        style="text-decoration: none; font-size:20px">📷 Instagram</a>
     <a href="https://www.instagram.com/manisha_m.a.l.i"\
        style="text-decoration: none; font-size:20px">🚀 Github</a>
</div>
""", unsafe_allow_html=True)
