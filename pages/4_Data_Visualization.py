import streamlit as st
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from visualization import *

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

selectbox_column, empty_column, data_column = st.columns([55,4,85])

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
        quater = st.selectbox("quater", ('q1', 'q2', 'q3', 'q4'), key='quater', label_visibility='collapsed')
        
    col8, col9 = st.columns([30,1])
 
        
with data_column:
    
    if options == 'Transactions':
        if year == year:
            if quater == quater:
                
                with col8:
                    transaction_questions = st.selectbox('Transactions:', ['Tap to select',
                                                                            'Total transaction amount for each payment type',
                                                                            'Top 10 state transactions amount',
                                                                            'Top 10 state transactions count',
                                                                            'Top 10 district transactions amount',
                                                                            'Top 10 district transactions count',
                                                                            'Top 10 pincode transactions amount',
                                                                            'Top 10 pincode transactions count'])

                if transaction_questions == 'Total transaction amount for each payment type':
                    
                    figure = px.pie(total_transactions(year, quater), values='transaction amount', 
                                        names='transaction type', 
                                        color_discrete_sequence=px.colors.qualitative.Pastel)
                    figure.update_layout(width=600, height=450)
                    figure.update_traces(rotation=90)
                    figure.update_traces(hole=0.4)
                    st.plotly_chart(figure)
                    
                elif transaction_questions == 'Top 10 state transactions amount':
                    figure = px.bar(top_state_transactions_amount(year, quater), x="transaction amount", 
                                        y="state", orientation='h', 
                                        color_continuous_scale= px.colors.diverging.Spectral, 
                                        color= 'transaction amount', 
                                        hover_data=["state", "transaction amount"], 
                                        height=420, width=700)
                    st.plotly_chart(figure)
                    
                elif transaction_questions == 'Top 10 state transactions count':
                    figure = px.bar(top_state_transactions_count(year, quater), x="transaction count", 
                                        y="state", orientation='h', 
                                        color_continuous_scale= px.colors.diverging.Spectral_r, 
                                        color= 'transaction count', 
                                        hover_data=["state", "transaction count"], 
                                        height=420, width=700)
                    st.plotly_chart(figure)
                    
                elif transaction_questions == 'Top 10 district transactions amount':
                    figure = px.bar(top_district_transactions_amount(year, quater), x="transaction amount", 
                                        y="district", orientation='h', 
                                        color_discrete_sequence=px.colors.carto.Tropic,
                                        color= 'district', 
                                        hover_data=["district", "transaction amount"], 
                                        height=420, width=700)
                    st.plotly_chart(figure)
                    
                elif transaction_questions == 'Top 10 district transactions count':
                    figure = px.bar(top_district_transactions_count(year, quater), x="transaction count", 
                                        y="district", orientation='h', 
                                        color_discrete_sequence=px.colors.sequential.YlOrRd, 
                                        color= 'district', 
                                        hover_data=["district", "transaction count"], 
                                        height=420, width=700)
                    st.plotly_chart(figure)
                    
                elif transaction_questions == 'Top 10 pincode transactions amount':
                    figure = px.bar(top_pincode_transactions_amount(year, quater), x="transaction amount", 
                                        y="pincode", orientation='h', 
                                        color_continuous_scale=px.colors.sequential.Sunsetdark,
                                        color= 'pincode', 
                                        hover_data=["pincode", "transaction amount"], 
                                        height=420, width=700)
                    st.plotly_chart(figure)
                    
                elif transaction_questions == 'Top 10 pincode transactions count':
                    figure = px.bar(top_pincode_transactions_count(year, quater), x="transaction count", 
                                        y="pincode", orientation='h', 
                                        color_continuous_scale=px.colors.colorbrewer.Set2, 
                                        color= 'pincode', 
                                        hover_data=["pincode", "transaction count"], 
                                        height=420, width=700)
                    st.plotly_chart(figure)
                    
    if options == 'Users':
        if year == year:
            if quater == quater:
                
                with col8:
                    
                    user_questions = st.selectbox('Users:', ['Tap to select',
                                                             'Top 10 user count by brand',
                                                             'Top 10 state user count by brand',
                                                             'Top 10 state registered user count',
                                                             'Top 10 district registered user count',
                                                             'Top 10 pincode registered user count'])
                
                if user_questions == 'Top 10 user count by brand':
                    figure = px.bar(user_brand_count(year, quater), x='brand', 
                                    y='user count', 
                                    hover_data=['brand', 'user count'],
                                    color='user count', 
                                    color_discrete_sequence=px.colors.colorbrewer.Set2, 
                                    labels={'brand' : 'brand','user count':'user count'}, 
                                    height=400)
                    figure.update_layout(xaxis={'type': 'category'}, yaxis={'title': 'user count'},)
                    st.plotly_chart(figure)
                    
                elif user_questions == 'Top 10 state user count by brand':
                    figure = px.density_heatmap(user_brand_count_state(year, quater), 
                                                x='brand',
                                                y='state',
                                                z='user count',
                                                color_continuous_scale=px.colors.sequential.Purp_r,
                                                height=420,
                                                width=800)
                    st.plotly_chart(figure)
                    
                elif user_questions == 'Top 10 state registered user count':
                    
                    figure = px.scatter(top_user_state(year, quater), 
                                        x='user count',
                                        y='state',
                                        color='state',
                                        size=pd.to_numeric(top_user_state(year, quater)['user count']),
                                        size_max=40,
                                        hover_data=['state', 'user count'],
                                        height=500)
                    
                    st.plotly_chart(figure)

                elif user_questions == 'Top 10 district registered user count':
                    
                    figure = px.scatter(top_user_district(year, quater), 
                                        x='user count',
                                        y='district',
                                        color='district',
                                        size=pd.to_numeric(top_user_district(year, quater)['user count']),
                                        size_max=40,
                                        hover_data=['district', 'user count'],
                                        height=500)
                    
                    st.plotly_chart(figure)
                    
                elif user_questions == 'Top 10 pincode registered user count':
                    
                    figure = px.bar(top_user_pincode(year, quater), x='pincode', 
                                    y='state', 
                                    hover_data=['state','pincode', 'user count'],
                                    color='user count', 
                                    color_discrete_sequence=px.colors.colorbrewer.Set2,
                                    height=400)
                    figure.update_layout(xaxis={'type': 'category'}, yaxis={'title': 'state'},)
                    st.plotly_chart(figure)


