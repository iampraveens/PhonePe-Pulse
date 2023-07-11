import streamlit as st
from PIL import Image
import locale
from extraction import *
from transactions import *
from users import *

image = Image.open('phonepe_logo.png')
page_title = 'PhonePe Pulse'
page_icon = image
layout = 'wide'

st.set_page_config(page_title=page_title,
                   page_icon=page_icon,
                   layout=layout
                   )

st.sidebar.success('Select a page above', icon='🚨')

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

selectbox_column, empty_column, data_column = st.columns([55,20,105])


with selectbox_column:
    
    st.write("<style>div.row-widget.stButton > button {color: white !important;}</style>", unsafe_allow_html=True)

    st.button('All India', disabled=True)
    col4, col5 = st.columns([8, 8])

    with col4:
        options = st.selectbox("options", ('Transactions', 'Users'), key="options", label_visibility='collapsed')

    with col5:
        year = st.selectbox("year", range(2018, 2023), key="year", label_visibility='collapsed')
        
    col6, col7 = st.columns([7, 7])

    with col6:
        quater = st.selectbox("quater", ('q1', 'q2', 'q3', 'q4'), key='quater', label_visibility='collapsed')
        

        
# col8, col9 = data_column.columns([15,4])

with data_column:
    
    if options == 'Transactions':
        if year == year:
            if quater == quater:
                st.markdown('<h1 style="color: #06bad4; font-size: 37px;">Transactions</h1>', unsafe_allow_html=True)
                st.write('All PhonePe transactions (UPI + Cards + Wallets)')
                all_trans = transactions(year, quater)['All PhonePe transactions'].apply(lambda x: '{:,}'.format(x)).values[0]
                colored1 = f'<span style="color: #06bad4;font-size: 23px; font-weight: bold;">{all_trans}</span>'
                st.markdown(colored1, unsafe_allow_html=True)
                
                col8, col9 = st.columns([8,14])
                
                with col8:
                    st.write("Total payment value")
                    total_payment = transactions(year, quater)['Total payment value'].apply(lambda x: '₹{:,.0f} Cr'.format(x/10000000)).values[0]
                    colored2 = f'<span style="color: #06bad4;font-size: 23px; font-weight: bold;">{total_payment}</span>'
                    st.markdown(colored2, unsafe_allow_html=True)
                with col9:
                    st.write("Avg. transaction value")
                    avg_trans = transactions(year, quater)['Avg. transaction value'].apply(lambda x: '₹{:,.0f}'.format(x)).values[0]
                    colored3 = f'<span style="color: #06bad4;font-size: 23px; font-weight: bold;">{avg_trans}</span>'
                    st.markdown(colored3, unsafe_allow_html=True)
                
                col10, col11 = st.columns([8,14])
                    
                with col10:
    
                    st.markdown('<h1 style="color: #06bad4; font-size: 37px;">Categories</h1>', unsafe_allow_html=True)
                    st.write('Recharge & bill payments')
                    st.write('Peer-to-peer payments')
                    st.write('Merchant payments')
                    st.write('Financial Services')
                    st.write('Others')
                    
                with col11:
                    locale.setlocale(locale.LC_ALL, 'en_IN')
                    st.markdown("""<hr style="height:12.4px;border:none;color:#210d38;background-color:#210d38;" /> """, unsafe_allow_html=True)
                    recharge = transactions_categories(year, quater)['Recharge & bill payments'].apply(lambda x: locale.format_string('%d', x, grouping=True)).values[0]
                    colored4 = f'<span style="color: #06bad4;font-size: 17px; font-weight: bold;">{recharge}</span>'
                    st.markdown(colored4, unsafe_allow_html=True)
                    
                    peer = transactions_categories(year, quater)['Peer-to-peer payments'].apply(lambda x: locale.format_string('%d', x, grouping=True)).values[0]
                    colored5 = f'<span style="color: #06bad4;font-size: 17px; font-weight: bold;">{peer}</span>'
                    st.markdown(colored5, unsafe_allow_html=True)
                    
                    merchant = transactions_categories(year, quater)['Merchant payments'].apply(lambda x: locale.format_string('%d', x, grouping=True)).values[0]
                    colored6 = f'<span style="color: #06bad4;font-size: 17px; font-weight: bold;">{merchant}</span>'
                    st.markdown(colored6, unsafe_allow_html=True)
                    
                    financial = transactions_categories(year, quater)['Financial Services'].apply(lambda x: locale.format_string('%d', x, grouping=True)).values[0]
                    colored7 = f'<span style="color: #06bad4;font-size: 17px; font-weight: bold;">{financial}</span>'
                    st.markdown(colored7, unsafe_allow_html=True)
                    
                    others = transactions_categories(year, quater)['Others'].apply(lambda x: locale.format_string('%d', x, grouping=True)).values[0]
                    colored8 = f'<span style="color: #06bad4;font-size: 17px; font-weight: bold;">{others}</span>'
                    st.markdown(colored8, unsafe_allow_html=True)
                    
    
        
                tab1, tab2, tab3 = st.tabs([' State ', ' District ', ' Pincode '])
                
                with tab1:
                    st.markdown('<h1 style="color: #06bad4; font-size: 25px;">Top 10 states</h1>', unsafe_allow_html=True)
                    col12, col13 = st.columns([8,14])
                    
                    with col12:
                        for rows in transactions_top_state(year, quater)['State']:
                            state = rows.capitalize()
                            st.write(state)
                            
                    with col13:
                        for rows in transactions_top_state(year, quater)['Total transaction count']:
                            if rows >= 10000000:
                                formatted_value = locale.format_string('%.2fCr', rows / 10000000, grouping=True)
                                colored9 = f'<span style="color: #06bad4;font-size: 16px; font-weight: bold;">{formatted_value}</span>'
                                st.markdown(colored9, unsafe_allow_html=True)
                            else:
                                formatted_value = locale.format_string('%.2fL', rows / 100000, grouping=True)
                                colored9 = f'<span style="color: #06bad4;font-size: 16px; font-weight: bold;">{formatted_value}</span>'
                                st.markdown(colored9, unsafe_allow_html=True)
                            
                with tab2:
                    st.markdown('<h1 style="color: #06bad4; font-size: 25px;">Top 10 districts</h1>', unsafe_allow_html=True)
                    col14, col15 = st.columns([8,14])
                    
                    with col14:
                        for rows in transactions_top_district(year, quater)['District']:
                            district = rows.capitalize()
                            st.write(district)
                            
                    with col15:
                        for rows in transactions_top_district(year, quater)['Total transaction count']:
                            if rows >= 10000000:
                                formatted_value = locale.format_string('%.2fCr', rows / 10000000, grouping=True)
                                colored10 = f'<span style="color: #06bad4;font-size: 16px; font-weight: bold;">{formatted_value}</span>'
                                st.markdown(colored10, unsafe_allow_html=True)
                            else:
                                formatted_value = locale.format_string('%.2fL', rows / 100000, grouping=True)
                                colored10 = f'<span style="color: #06bad4;font-size: 16px; font-weight: bold;">{formatted_value}</span>'
                                st.markdown(colored10, unsafe_allow_html=True)
                                
                with tab3:
                    st.markdown('<h1 style="color: #06bad4; font-size: 25px;">Top 10 pincodes</h1>', unsafe_allow_html=True)
                    col16, col17 = st.columns([8,14])
                    
                    with col16:
                        for rows in transactions_top_pincode(year, quater)['Pincode']:
                            st.markdown(f"<span style='font-size: 16px;'>{rows}</span>", unsafe_allow_html=True)
                            
                    with col17:
                        for rows in transactions_top_pincode(year, quater)['Total transaction count']:
                            if rows >= 10000000:
                                formatted_value = locale.format_string('%.2fCr', rows / 10000000, grouping=True)
                                colored11 = f'<span style="color: #06bad4;font-size: 16px; font-weight: bold;">{formatted_value}</span>'
                                st.markdown(colored11, unsafe_allow_html=True)
                            else:
                                formatted_value = locale.format_string('%.2fL', rows / 100000, grouping=True)
                                colored12 = f'<span style="color: #06bad4;font-size: 16px; font-weight: bold;">{formatted_value}</span>'
                                st.markdown(colored12, unsafe_allow_html=True)
            
    elif options == 'Users':
        if year == year:
            if quater == quater:
                st.markdown('<h1 style="color: #c386d4; font-size: 37px;">Users</h1>', unsafe_allow_html=True)
                st.write(f'Registered PhonePe users till {quater} {year}')
                reg_usr = users(year, quater)['Registered PhonePe users'].apply(lambda x: locale.format_string('%d', x, grouping=True)).values[0]
                colored13 = f'<span style="color: #c386d4;font-size: 23px; font-weight: bold;">{reg_usr}</span>'
                st.markdown(colored13, unsafe_allow_html=True)
                
                st.write(f'PhonePe app opens in {quater} {year}')
                reg_usr = users(year, quater)['PhonePe app opens'].apply(lambda x: locale.format_string('%d', x, grouping=True)).values[0]
                colored15 = f'<span style="color: #c386d4;font-size: 23px; font-weight: bold;">{reg_usr}</span>'
                st.markdown(colored15, unsafe_allow_html=True)
                
                tab4, tab5, tab6 = st.tabs([' State ', ' District ', ' Pincode '])
                
                with tab4:
                    st.markdown('<h1 style="color: #c386d4; font-size: 25px;">Top 10 states</h1>', unsafe_allow_html=True)
                    col18, col19 = st.columns([8,14])
                    
                    with col18:
                        for rows in users_top_state(year, quater)['State']:
                            state = rows.capitalize()
                            st.write(state)
                            
                    with col19:
                        for rows in users_top_state(year, quater)['Total registered users']:
                            if rows >= 10000000:
                                formatted_value = locale.format_string('%.2fCr', rows / 10000000, grouping=True)
                                colored16 = f'<span style="color: #c386d4;font-size: 16px; font-weight: bold;">{formatted_value}</span>'
                                st.markdown(colored16, unsafe_allow_html=True)
                            else:
                                formatted_value = locale.format_string('%.2fL', rows / 100000, grouping=True)
                                colored17 = f'<span style="color: #c386d4;font-size: 16px; font-weight: bold;">{formatted_value}</span>'
                                st.markdown(colored17, unsafe_allow_html=True)
                            
                with tab5:
                    st.markdown('<h1 style="color: #c386d4; font-size: 25px;">Top 10 districts</h1>', unsafe_allow_html=True)
                    col20, col21 = st.columns([8,14])
                    
                    with col20:
                        for rows in users_top_district(year, quater)['District']:
                            district = rows.capitalize()
                            st.write(district)
                            
                    with col21:
                        for rows in users_top_district(year, quater)['Total registered users']:
                            if rows >= 10000000:
                                formatted_value = locale.format_string('%.2fCr', rows / 10000000, grouping=True)
                                colored18 = f'<span style="color: #c386d4;font-size: 16px; font-weight: bold;">{formatted_value}</span>'
                                st.markdown(colored18, unsafe_allow_html=True)
                            else:
                                formatted_value = locale.format_string('%.2fL', rows / 100000, grouping=True)
                                colored19 = f'<span style="color: #c386d4;font-size: 16px; font-weight: bold;">{formatted_value}</span>'
                                st.markdown(colored19, unsafe_allow_html=True)
                                
                with tab6:
                    st.markdown('<h1 style="color: #c386d4; font-size: 25px;">Top 10 pincodes</h1>', unsafe_allow_html=True)
                    col22, col23 = st.columns([8,14])
                    
                    with col22:
                        for rows in users_top_pincode(year, quater)['Pincode']:
                            st.markdown(f"<span style='font-size: 16px;'>{rows}</span>", unsafe_allow_html=True)
                            
                    with col23:
                        for rows in users_top_pincode(year, quater)['Total registered users']:
                            if rows >= 10000000:
                                formatted_value = locale.format_string('%.2fCr', rows / 10000000, grouping=True)
                                colored20 = f'<span style="color: #c386d4;font-size: 16px; font-weight: bold;">{formatted_value}</span>'
                                st.markdown(colored20, unsafe_allow_html=True)
                            else:
                                formatted_value = locale.format_string('%.2fL', rows / 100000, grouping=True)
                                colored21 = f'<span style="color: #c386d4;font-size: 16px; font-weight: bold;">{formatted_value}</span>'
                                st.markdown(colored21, unsafe_allow_html=True)
                
