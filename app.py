import streamlit as st
import pandas as pd
from dotenv import load_dotenv
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
    page_icon=":books:",
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
    </style>
    """, unsafe_allow_html=True)
# Initialize session state for the DataFrame
if 'df' not in st.session_state:
    st.session_state.df = None

# Sidebar menu
with st.sidebar:
    # Title with centered alignment
    st.markdown("<h2 style='text-align: center;'>Menu</h2>", unsafe_allow_html=True)

    # Subtitle with centered alignment
    st.markdown("<h4 style='text-align: center;'>Navigate through the sections:</h4>", unsafe_allow_html=True)
    
    selected = option_menu(
        'Main Menu',
        ['Home', 'Competitor Analysis', 'Issues Analysis'],
        icons=['house', 'bar-chart-line', 'list-check'],
        default_index=0,
        menu_icon="cast"
    )

if selected == "Home":
    home()

elif selected == "Competitor Analysis":
    competitor()

elif selected == "Issues Analysis":
    issues()

