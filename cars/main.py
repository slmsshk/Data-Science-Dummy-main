import streamlit as st
import numpy as np
import pandas as pd
from UI import *

st.set_page_config('Regression Model','✅')
st.write(f"<h1 style=color:red;text-align:center>Linear Regression</h1>",unsafe_allow_html=True)
st.divider()

st.write("<p style=color:orange;>This is my notebook on Linear Regression</p>",unsafe_allow_html=True)
st.balloons()
st.snow()

st.write("Knowledge checkpoint")
if st.button('Submit'):
    q1 = st.text_input("What is regression analysis?", value='', key='q1')
    if q1 != '':
        # Process the user's answer or perform any desired actions based on the submission
        st.write(f"Your answer: {q1}")