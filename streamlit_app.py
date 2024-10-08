from PIL import Image
import requests
import streamlit as st
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Vanesa Hercules")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- STYLING ----
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_url = "https://assets8.lottiefiles.com/packages/lf20_w51pcehl.json"
lottie_json = load_lottieurl(lottie_url)
img_gmail = Image.open("images/gmail_stock_img.jpg")

# ---- SCROLL TO TOP  ----
if "counter" not in st.session_state:
    st.session_state.counter = 1

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi! I'm Vanesa :wave:")
    st.markdown("<h1 style='text-align: center;'>Data Management, Privacy & AI</h1>", unsafe_allow_html=True)

# ---- BODY ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About me")
        st.write("##")
        st.write(
            """
            Experienced technology consultant specializing in data management, privacy & AI. 
            
            Master's degree in Applied Computer Science. 
            
            Dabbling in automation, data engineering & robotics.

            """
        )
    with right_column:
        st.write("##")
        st_lottie(lottie_json, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My latest project")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_gmail)
    with text_column:
        st.subheader("Extract Unsubscribe Links from Emails")
        st.write(
            """
            Using Google Apps Script and Python, this project gathers messages from Gmail and extracts unsubscribe links to Google Sheets.
            """
        )
        st.markdown("[Read more >>](https://medium.com/@vnhercules/extract-unsubscribe-links-from-emails-using-apps-script-and-python-800afb8e0ec6)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.markdown("<h1 style='text-align: center;'>🎉</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Thanks for stopping by!</h3>", unsafe_allow_html=True)
    st.write("##")
with st.container():
    col1, col2, col3, col4, col5= st.columns((2.25,1,1,1,2))
    with col1:
        st.empty()
    with col2:
        st.write("[Email](mailto:vnhercules@gmail.com)")
    with col3:
        st.empty()
    with col4:
        st.write("[GitHub](https://github.com/vnhercules)")
    with col5:
        st.empty()
with st.container():
    st.write("##")
    col1, col2, col3, col4, col5= st.columns((2,1,1,1,2))
    with col1:
        st.empty()
    with col2:
        st.empty()
    with col3:
        if st.button("Back to Top"):
            st.session_state.counter += 1
    with col4:
        st.empty()
    with col5:
        st.empty()

components.html(
    f"""
        <p>{st.session_state.counter}</p>
        <script>
            window.parent.document.querySelector('section.main').scrollTo(0, 0);
        </script>
    """,
    height=0
)
