#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 14:40:39 2023

@author: camus
"""

import streamlit as st
import pandas as pd
from streamlit_elements import elements, dashboard, mui, nivo, html


# Function to set theme
st.set_page_config(layout="wide", initial_sidebar_state="expanded", page_icon="🧊")

# Title of the application
st.title('Dashboard Builder Application')

# Section for data visualization
if 'dataset' not in st.session_state:
    st.title('Data not loaded.')
else:        
    st.write('Loaded Data:')
    st.write(st.session_state['dataset'])

# Show the side bar image
def display_image_page():
    if 'logo' not in st.session_state:
        st.sidebar.header("No image loaded yet.")
    else:
        st.sidebar.image(st.session_state['logo'],use_column_width=True)
        
display_image_page()