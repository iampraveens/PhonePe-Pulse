import streamlit as st
from PIL import Image
from extraction import *
from streamlit_extras.dataframe_explorer import dataframe_explorer
import time

image = Image.open('phonepe_logo.png')
page_title = 'PhonePe Pulse'
page_icon = image
layout = 'wide'

st.set_page_config(page_title=page_title,
                   page_icon=page_icon,
                   layout=layout
                   )

hide_style = '''
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            <style>
            
            '''
            
header_style = '''
             <style>
             .navbar {
                 position: fixed;
                 top: 0;
                 left: 0;
                 width: 100%;
                 z-index: 1;
                 display: flex;
                 justify-content: center;
                 align-items: center;
                 height: 80px;
                 background-color: #402866;
                 box-sizing: border-box;
             }
             
             .navbar-brand {
                 color: white !important;
                 font-size: 18px;
                 text-decoration: none;
                 margin-right: auto;
                 margin-left: 20px;
             }
             
             .navbar-brand img {
                margin-bottom: 6px;
                margin-right: 1px;
                width: 35px;
                height: 35px;
                justify-content: center;
            }
            
            /* Add the following CSS to change the color of the text */
            .navbar-brand span {
                color: #9973d5;
                justify-content: center;
            }
            
             </style>
             
             <nav class="navbar">
                 <div class="navbar-brand">
                <img src="https://img.uxwing.com/wp-content/themes/uxwing/download/brands-social-media/phonepe-logo-icon.svg" alt="Logo">
                PhonePe Pulse <span> | THE BEAT OF PROGRESS</span>
                 </div>
             </nav>
               '''
            
st.markdown(hide_style, unsafe_allow_html=True)

st.markdown(header_style, unsafe_allow_html=True)

st.write("<style>div.row-widget.stButton > button {color: white !important;}</style>", unsafe_allow_html=True)

st.button('All India', disabled=True)

# st.markdown('''
#     <style>
#     .st-bn {
#         width: 200px !important; /* Adjust width as needed */
#         height: 40px !important; /* Adjust height as needed */
#     </style>
# ''', unsafe_allow_html=True)

# # Create two columns
# col1, col2 = st.columns(2)

# # Add selectboxes to the columns
# with col1:
#     option1 = st.selectbox("", ('Transactions', 'Users'), label_visibility='collapsed')

# with col2:
#     option2 = st.selectbox("", range(2018, 2023), label_visibility='collapsed')

st.markdown('''
    <style>
    .st-bn {
        width: 170px !important; /* Adjust width as needed */
        height: 40px !important; /* Adjust height as needed */
    }

    .custom-container {
        display: flex;
        align-items: center;
    }

    .custom-column {
        width: 120px !important;
        margin-right: 1px; /* Adjust the margin as needed */
    }
    .custom-selectbox {
        width: 120px !important; /* Adjust width as needed */
    }
    </style>
''', unsafe_allow_html=True)

# Create two columns with adjusted widths
col1, col2 = st.columns([1, 7])

# Add selectboxes to the columns
with col1:
    options = st.selectbox("", ('Transactions', 'Users'), key="options", label_visibility='collapsed')

with col2:
    year = st.selectbox("", range(2018, 2023), key="year", label_visibility='collapsed')
    
quater = st.selectbox("", ('q1', 'q2', 'q3', 'q4'), key='quater', label_visibility='collapsed')
    

















            

