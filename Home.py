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


def color_properties():

    # Side bar section Title
    st.sidebar.header("Chart Color Properties")
    
    col1,col2,col3 = st.sidebar.columns(3)
    # Data colors
    with col1:
        st.session_state['data_color'] = st.color_picker('Data', '#FF0000')
    
    with col2:
    # Background color
        st.session_state['bkg_color'] = st.color_picker('Background', '#000000')
    
    with col3:
    # Text color
        st.session_state['text_color'] = st.color_picker('Text', '#FFFFFF')    


# Function to load data
@st.cache_data()
def load_data():
    uploaded_file = st.file_uploader(":file_folder: Everything begins with data: Upload your dataset")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.session_state['dataset'] = data
        return data
    

# Title of the application
st.title('Dashboard Builder Application')

# Loading data
data = load_data()

# Main section for data visualization
if data is not None:
    st.write('Loaded Data:')
    st.write(st.session_state['dataset'])
    
    # Header for dataset properties
    st.sidebar.header('Dataset')
    
    
    # Process of filtering the data for plotting
    data = df_filter(st.session_state['dataset'])
    st.session_state['data_filtered'] = data
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
            st.session_state['data_x'] = data_x
            data = data.groupby(x).mean()
            
            y = st.sidebar.selectbox('Choose y-axis data', options=data.columns)
            st.session_state['y'] = y
            data_y = list(data[y])
            st.session_state['data_y'] = data_y
            
            st.sidebar.header("Chart Properties")
            
            # Font size
            st.session_state['font_size'] = st.sidebar.slider("Font size: ", 0.0, 18.0, 11.0)
            # User defines x and y labels
            st.session_state['y_label'] = st.sidebar.text_input('Insert y label', st.session_state['y'])
            st.session_state['x_label'] = st.sidebar.text_input('Insert x label', st.session_state['x'])
            
            
            # User defines chart title
            st.session_state['title'] = st.sidebar.text_input('Insert Chart Title', 'CHART TITLE')
            
            if plot_type == 'Line':
                st.session_state['line_width'] = st.sidebar.slider("Line width: ", 0.0, 8.0, 2.0)
                color_properties()
                dcp.add_dashboard_line(data_x,data_y)
            elif plot_type == 'Bar':
                st.session_state['bar_width'] = st.sidebar.slider("Bar width: ", 0.0, 1.0, 0.4)
                color_properties()
                dcp.add_dashboard_bar(data_x,data_y)
            elif plot_type == 'Scatter':
                st.session_state['marker_size'] = st.sidebar.slider("Marker size: ", 1, 20, 10)
                color_properties()
                dcp.add_dashboard_scatter(data_x, data_y)