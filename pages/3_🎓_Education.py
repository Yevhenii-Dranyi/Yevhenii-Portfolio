import streamlit as st


st.set_page_config(
    page_title="Education",
    page_icon="🎓",
    layout="wide",
)

st.title("🎓 Education")
st.write("Here are my educational details:")

st.markdown("""
<div style="background-color: #f0f0f0; margin-top:20px; padding: 20px;
text-align: center; border-radius: 15px;">
    <p><b>🏛️ University:</b> Shivaji University, Kolhapur</p>
    <p><b>🏫 College Name:</b> Walchand College of Engineering, Sangli</p>
    <p><b>💻 Branch:</b> Computer Science and Engineering</p>
    <p><b>📊 CGPA:</b> 8.81</p>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div style="background-color: #f0f0f0; padding: 20px; text-align: center;
margin-top:20px; border-radius: 15px;">
    <p><b>🏛️ University:</b> Maharashtra State Board of Technical Education</p>
    <p>
        <b>🏫 College Name:</b>
        Government Residential Women's Polutechnic, Latur
    </p>
    <p><b>💻 Branch:</b> Computer Engineering</p>
    <p><b>📊 Percentage:</b> 96.57</p>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div style="background-color: #f0f0f0; padding: 20px; text-align: center;
margin-top:20px; border-radius: 15px;">
    <p><b>🏛️ University:</b>  Maharashtra State Board</p>
    <p><b>🏫 College Name:</b>Loknayak Vidyalay, Naigaon</p>
    <p><b>💻 Standard:</b> 10th</p>
    <p><b>📊 Percentage:</b> 90.20</p>
</div>
""", unsafe_allow_html=True)
