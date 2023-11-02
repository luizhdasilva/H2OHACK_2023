#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on October 2023

@author: H2Oh My Goodnes Team
"""

import streamlit as st
import plotly.express as px
from plotly.io import to_image
import pandas as pd
import numpy as np
from streamlit_elements import dashboard, elements, mui, nivo, html
import dashboard_chart_plot as dcp
from df_filter import df_filter, df_filter_container

# Function to set theme
st.set_page_config(layout="wide", initial_sidebar_state="expanded", page_icon="🧊")

# Logo application
st.sidebar.title("Upload Your Beautiful Logo")
def logoside():

    uploaded_logo = st.sidebar.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    
    if uploaded_logo is not None:
        st.sidebar.image(uploaded_logo, use_column_width=True)
        st.session_state['logo'] = uploaded_logo
        logo = uploaded_logo
        return logo
        
logo = logoside()

# Function to load data
def load_data():
    uploaded_file = st.file_uploader(":file_folder: Everything begins with data: Upload your dataset")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.session_state['dataset'] = data
        return data
    

# Title of the application
st.title('Dashboard Builder Application')

# Sidebar for data loading
data = load_data()

# Main section for data visualization
if data is not None:
    st.write('Loaded Data:')
    st.write(data)
    
    data = df_filter(data)
    
    if 'characteristic_name' in data.columns:
        characteristic_name_unique = data['characteristic_name'].unique()
        characteristic_name = st.multiselect(
            "Choose characteristics", characteristic_name_unique, 
            characteristic_name_unique[0]
            )
        st.session_state['characteristic'] = characteristic_name
    if not characteristic_name:
        st.error("Please select at least one characteristics.")
    else:
        data = data[data['characteristic_name'].isin(characteristic_name)]
        st.session_state['dataset'] = data
        

    site_unique = data['site'].unique()
    site_name = st.sidebar.multiselect(
        "Choose site", site_unique, 
        site_unique[0]
        )
    st.session_state['site'] = site_name
    if not site_name:
        st.error("Please select at least one characteristics.")
    else:
        data = data[data['site'].isin(site_name)]
        st.session_state['dataset'] = data

    st.write('Plotting Data:')

    # Sidebar for plot type
    plot_types = ['Bar', 'Line']
    plot_type = st.sidebar.selectbox('Select Plot Type', plot_types)
    st.session_state['plot_type'] = plot_type
    
    # Sidebar for user inputs
    if plot_type == 'Line':
        x = st.sidebar.selectbox('Choose x-axis data', options=data.columns)
        st.session_state['x'] = x
        y = st.sidebar.selectbox('Choose y-axis data', options=data.columns)
        st.session_state['y'] = y
        # Prepare the figure object
        if 'x' in st.session_state and 'y' in st.session_state:
            data_x = list(data[x])
            data_y = list(data[y])
            dcp.add_dashboard_line(data_x,data_y)

        #st.plotly_chart(fig)

    elif plot_type == 'Bar':
        x = st.sidebar.selectbox('Choose x-axis data', options=data.columns)
        st.session_state['x'] = x
        y = st.sidebar.selectbox('Choose y-axis data', options=data.columns)
        st.session_state['y'] = y
        if 'x' in st.session_state and 'y' in st.session_state:
            data_x = list(data[x])
            data_y = list(data[y])
            dcp.add_dashboard_bar(data_x,data_y)
        #st.plotly_chart(fig)
        
        
