#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on October 2023

@author: H2Oh My Goodnes Team
"""

import streamlit as st
import plotly.express as px
import pandas as pd
import datetime as dt 

from pandas.api.types import is_datetime64_any_dtype as is_datetime

from df_filter import (df_filter, df_filter_container)

# Function to load data
def load_data():
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        return data

# Function to set theme
st.set_page_config(layout="wide", initial_sidebar_state="expanded", page_icon="🧊")

# Title of the application
st.title('Dashboard Builder Application')


# Sidebar for data loading
st.sidebar.header('Upload Data')
data = load_data()

# Main section for data visualization
if data is not None:

    data = df_filter(data)

    st.write('Loaded Data:')
    st.write(data)

    st.write('Plotting Data:')

    # Sidebar for plot type
    plot_types = ['Line', 'Bar']
    plot_type = st.sidebar.selectbox('Select Plot Type', plot_types)

    # Sidebar for user inputs
    if plot_type == 'Line':
        x = st.sidebar.selectbox('Choose x-axis data', options=data.columns)
        y = st.sidebar.selectbox('Choose y-axis data', options=data.columns)
        fig = px.line(data, x=x, y=y, title='Line Chart')
        st.plotly_chart(fig)

    elif plot_type == 'Bar':
        x = st.sidebar.selectbox('Choose x-axis data', options=data.columns)
        y = st.sidebar.selectbox('Choose y-axis data', options=data.columns)
        fig = px.bar(data, x=x, y=y, title='Bar Chart')
        st.plotly_chart(fig)
