#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 14:01:42 2023

@author: camus
"""

import streamlit as st
import pandas as pd
import numpy as np
import dashboard_chart_plot as dcp
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



if 'plot_type' in st.session_state:
    # Prepare the figure object
    
        if st.session_state['plot_type'] == 'Line':
            dcp.add_dashboard_line(st.session_state['data_x'],st.session_state['data_y'])
        elif st.session_state['plot_type'] == 'Bar':
            dcp.add_dashboard_bar(st.session_state['data_x'],st.session_state['data_y'])
        elif st.session_state['plot_type'] == 'Scatter':
            dcp.add_dashboard_scatter(st.session_state['data_x'],st.session_state['data_y'])