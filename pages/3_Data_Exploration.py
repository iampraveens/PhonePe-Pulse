import streamlit as st
from PIL import Image
from extraction import *
from streamlit_extras.dataframe_explorer import dataframe_explorer
from transactions import *

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
                 margin-left: 50px;
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

st.markdown('<h1 style="color: #c386d4; font-size: 37px;">Data Exploration</h1>', unsafe_allow_html=True)

options = st.selectbox("Select one option below:", options=['Tap to select',
                                                            'Aggregated Transaction', 
                                                            'Aggregated User', 
                                                            'Map Transcation', 
                                                            'Map User', 
                                                            'Top Transaction', 
                                                            'Top User', 
                                                            'Top Transaction Pincodes', 
                                                            'Top User Pincodes'])

if options == 'Aggregated Transaction':
    filtered_df = dataframe_explorer(aggregated_transcation_state())
    st.dataframe(filtered_df, use_container_width=True)
    
elif options == 'Aggregated User':
    filtered_df = dataframe_explorer(aggregated_user_state())
    st.dataframe(filtered_df, use_container_width=True)
    
elif options == 'Map Transcation':
    filtered_df = dataframe_explorer(map_transcation_state())
    st.dataframe(filtered_df, use_container_width=True)
    
elif options == 'Map User':
    filtered_df = dataframe_explorer(map_user_state())
    st.dataframe(filtered_df, use_container_width=True)
    
elif options == 'Top Transaction':
    filtered_df = dataframe_explorer(top_transcation_state())
    st.dataframe(filtered_df, use_container_width=True)
    
elif options == 'Top User':
    filtered_df = dataframe_explorer(top_user_state())
    st.dataframe(filtered_df, use_container_width=True)
    
elif options == 'Top Transaction Pincodes':
    filtered_df = dataframe_explorer(top_transcation_state_pincode())
    st.dataframe(filtered_df, use_container_width=True)
    
elif options == 'Top User Pincodes':
    filtered_df = dataframe_explorer(top_user_state_pincode())
    st.dataframe(filtered_df, use_container_width=True)