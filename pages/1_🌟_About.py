import streamlit as st


st.set_page_config(
    page_title="About Me",
    page_icon="📚",
    layout="wide",
)

custom_css = """
<style>
    .header {
        font-size: 30px;
        font-weight: bold;
        color: #333;
    }
    .pad-left {
        margin-left: 40px;
        padding-left: 10px;
        position: relative;
        font-size: 18px;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

st.markdown(
    '<p class="header">👋 Hi there! I\'m Manisha Mali </p>',
    unsafe_allow_html=True
)
st.markdown(
    '<p class="pad-left">\
    A passionate individual with a flair for technology and a love for life.\
    </p>',
    unsafe_allow_html=True
)

st.subheader("🌟 Professional Summary")
st.write(
    "<p class='pad-left'>\
    • I hold a Bachelor's degree in Computer Science and Engineering (B.Tech).\
    </p>",
    unsafe_allow_html=True
)
st.write(
    "<p class='pad-left'>\
    • I'm dedicated to continuous learning and growth in the tech world.\
    </p>",
    unsafe_allow_html=True
)
st.markdown(
    "<p class='pad-left'>\
        • Let's embark on a journey of exploration and innovation together!\
    </p>",
    unsafe_allow_html=True
)

st.subheader("🌼 Hobbies")
st.write("<p class='pad-left'>• Gardening 🌱", unsafe_allow_html=True)
st.write("<p class='pad-left'>• Badminton 🏸", unsafe_allow_html=True)
st.write("<p class='pad-left'>• Kho Kho 🤸", unsafe_allow_html=True)
st.write("<p class='pad-left'>• Traveling ✈️", unsafe_allow_html=True)
st.write("<p class='pad-left'>• Learning new things 📚", unsafe_allow_html=True)
