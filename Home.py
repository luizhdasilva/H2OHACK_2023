#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on October 2023

@author: H2Oh My Goodnes Team
"""

import streamlit as st
import pandas as pd
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
st.session_state['dataset'] = data

# Main section for data visualization
if data is not None:
    st.write('Loaded Data:')
    st.write(data)
    
    data = df_filter(st.session_state['dataset'])

    st.write('Plotting Data:')

    # Sidebar for plot type
    plot_types = ['Line','Scatter','Bar']
    plot_type = st.sidebar.selectbox('Select Plot Type', plot_types)
    st.session_state['plot_type'] = plot_type
    
    # Sidebar for user inputs
    if 'plot_type' in st.session_state:
        x = st.sidebar.selectbox('Choose x-axis data', options=data.columns)
        st.session_state['x'] = x
        # Prepare the figure object
        if 'x' in st.session_state:
            
            data_x = list(data[x].unique())
            data = data.groupby(x).mean()
            
            y = st.sidebar.selectbox('Choose y-axis data', options=data.columns)
            st.session_state['y'] = y
            data_y = list(data[y])
            
            # User defines x and y labels
            st.session_state['y_label'] = st.sidebar.text_input('Insert y label', st.session_state['y'])
            st.session_state['x_label'] = st.sidebar.text_input('Insert x label', st.session_state['x'])
            
            # User defines chart title
            st.session_state['title'] = st.sidebar.text_input('Insert Chart Title', 'CHART TITLE')
            
            if plot_type == 'Line':
                dcp.add_dashboard_line(data_x,data_y)
            elif plot_type == 'Bar':
                dcp.add_dashboard_bar(data_x,data_y)
            elif plot_type == 'Scatter':
                dcp.add_dashboard_scatter(data_x, data_y)