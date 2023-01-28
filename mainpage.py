import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="CamCat Detector",
)

image = Image.open('cat2.png')
new_image = image.resize((200, 200))
st.image(new_image)

st.title('CamCat Detector')
st.header('A Border Gateway Anomalies Prediction App')
st.subheader('This app detects four types of viruses which helps to analyse and detect malware or other breaches.')

selected = option_menu(
    menu_title="Main Menu",
    options=["Nimda", "Slammer", "Code Red 1", "Moscow Blackout"],
    orientation="horizontal",
)

if selected == "Nimda":
    st.title(f"You have selected {selected}")
    url = "https://yogithaa5-nimda-nimda-prediction-49c8fd.streamlit.app/"
    st.header("[Detect Now!](%s)" % url)

if selected == "Slammer":
    st.title(f"You have selected {selected}")
    url = "https://yogithaa5-slammer-slammer-prediction-yll6jb.streamlit.app/"
    st.header("[Detect Now!](%s)" % url)

if selected == "Code Red 1":
    st.title(f"You have selected {selected}")
    url = "https://yogithaa5-codered1-codered1-prediction-1e8aet.streamlit.app/"
    st.header("[Detect Now!](%s)" % url)

if selected == "Moscow Blackout":
    st.title(f"You have selected {selected}")
    url = "https://yogithaa5-moscowblackout-moscow-prediction-67gyu8.streamlit.app/"
    st.header("[Detect Now!](%s)" % url)


