#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 14:01:42 2023

@author: camus
"""

import streamlit as st
import pandas as pd
import numpy as np
from streamlit_elements import elements, dashboard, mui, html

# Function to set themett
st.set_page_config(layout="wide", initial_sidebar_state="expanded", page_icon=":bar_chart:")

# Title of the application
st.title('Dashboard Builder Application')

# Show the side bar image
def display_image_page():
    if 'logo' not in st.session_state:
        st.sidebar.header("No image loaded yet.")
    else:
        st.sidebar.image(st.session_state['logo'],use_column_width=True)
        
display_image_page()

# Main section for data visualization
# Sidebar for user inputs
if st.session_state['plot_type'] == 'Line':
    fig = px.line(st.session_state['dataset'], 
                 x=st.session_state['x'], y=st.session_state['y'], title='Line Chart')
    st.plotly_chart(fig)

elif st.session_state['plot_type'] == 'Bar':

    fig = px.bar(st.session_state['dataset'],
                 x=st.session_state['x'], y=st.session_state['y'], title='Bar Chart')
    st.plotly_chart(fig)