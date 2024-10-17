import streamlit as st
import pandas as pd
from pathlib import Path
import os
from streamlit_option_menu import option_menu
import plotly.express as px
from collections import Counter
from home import home
from competitor import competitor
from issues import issues

st.set_page_config(
    page_title="Splashtop Content Analysis",
    page_icon=":chart:",
    layout="wide"
)

st.markdown("""
    <style>
        .intro {
            font-size: 18px;
            color: #4A4A4A;
        }
        .stApp {
            background-color: #f0f2f6;
        }
        .header {
            font-size: 24px;
            color: #003f5c;
            font-weight: bold;
            margin-bottom: 20px;
        } 
        .info-box {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        .sidebar .sidebar-content {
            background-color: #f8f9fa;
        }
        .sidebar .sidebar-content .stMarkdown {
            padding: 10px;
            border-radius: 5px;
            background-color: #e9ecef;
            margin-bottom: 10px;
        }
    </style>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>Splashtop Content Analysis</h2>", unsafe_allow_html=True)
    st.divider()
    selected = option_menu(
        'Navigation',
        ['Home', 'Competitor Analysis', 'Issues Analysis'],
        icons=['house', 'bar-chart-line', 'list-check'],
        default_index=0,
        menu_icon="cast"
    )
    st.divider()    
    st.markdown("""
    <div class='info-box'>
        <p>This application provides in-depth analysis of Splashtop content, including:</p>
        <ul>
            <li>Content analysis</li>
            <li>Competitor analysis</li>
            <li>Issues tracking</li>
        </ul>
        <p>Navigate through different sections to explore various aspects of the analysis.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown(
        '<h4>Made in &nbsp<img src="https://streamlit.io/images/brand/streamlit-mark-color.png" alt="Streamlit logo" height="16">&nbsp by <a href="https://github.com/naveen3830"> @Naveen</a></h4>',
            unsafe_allow_html=True,
        )
if selected == "Home":
    home()
    
elif selected == "Competitor Analysis":
    competitor()
    
elif selected == "Issues Analysis":
    issues()