import streamlit as st
from PIL import Image

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="Methodology"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Methodology (Flow Chart)")
image = Image.open('flowchart.jpg')
st.image(image)