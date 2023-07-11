import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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

selectbox_column, empty_column, map_column = st.columns([55,4,85])


with selectbox_column:
    
    st.write("<style>div.row-widget.stButton > button {color: white !important;}</style>", unsafe_allow_html=True)

    st.button('All India', disabled=True)
    col4, col5 = st.columns([8, 6])

    with col4:
        options = st.selectbox("options", ('Transactions', 'Users'), key="options", label_visibility='collapsed')

    with col5:
        year = st.selectbox("year", range(2018, 2023), key="year", label_visibility='collapsed')
        
    col6, col7 = st.columns([9, 7])

    with col6:
        quater = st.selectbox("quater", ('Q1', 'Q2', 'Q3', 'Q4'), key='quater', label_visibility='collapsed')
        
with map_column:
    
    transactions = pd.read_csv(r'D:\Phonepe Pulse\miscellaneous\geo_transactions.csv')
    users = pd.read_csv(r'D:\Phonepe Pulse\miscellaneous\geo_users.csv')
    
    filtered_transactions = transactions[(transactions['Year'] == year) & (transactions['Quarter'] == quater)]
    filtered_users = users[(users['Year'] == year) & (users['Quarter'] == quater)]
    
    if options == 'Transactions':
        if year == year:
            if quater == quater:
                
                geojson_file = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
                
                transactions['State'] = transactions['State'].str.replace('and ', '& ')
                transactions['State'] = transactions['State'].str.replace('Andaman & Nicobar Islands', 'Andaman & Nicobar')
                
                figure = px.choropleth(data_frame=filtered_transactions,
                      geojson=geojson_file,
                      featureidkey='properties.ST_NM',
                      locations='State',
                      projection='mercator',
                      hover_data={'Transaction_count': ':,', 'Transaction_amount': ':,'},
                      hover_name='State',
                      color='State',
                      color_continuous_scale=px.colors.colorbrewer.Set2,
                      scope='asia')
                figure.update_geos(fitbounds = "geojson",visible=False)
                figure.update_layout(margin={'r': 0, 't': 0, 'l': 0, 'b': 0})
                figure.update_layout(width=500, height=580)
                figure.update_layout(
                        geo=dict(bgcolor='rgba(0,0,0,0)'),
                        plot_bgcolor='rgba(0,0,0,0)', 
                        )
                        
                st.plotly_chart(figure, use_container_width=True)
                
    elif options == 'Users':
        if year == year:
            if quater == quater:
                
                geojson_file = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
                
                users['State'] = users['State'].str.replace('and ', '& ')
                users['State'] = users['State'].str.replace('Andaman & Nicobar Islands', 'Andaman & Nicobar')
                
                figure = px.choropleth(data_frame=filtered_users,
                    geojson=geojson_file,
                    featureidkey='properties.ST_NM',
                    locations='State',
                    projection='mercator',
                    color='Registered_user',
                    hover_data={'Registered_user': ':,'},
                    hover_name='State',
                    color_continuous_scale=px.colors.cyclical.Twilight,
                    scope='asia')
                figure.update_geos(fitbounds = "locations",visible=False)
                figure.update_layout(margin={'r': 0, 't': 0, 'l': 0, 'b': 0})
                figure.update_layout(width=500, height=550)
                figure.update_layout(
                    geo=dict(bgcolor='rgba(0,0,0,0)'),
                    plot_bgcolor='rgba(0,0,0,0)', 
                    )
                    
                st.plotly_chart(figure, use_container_width=True)