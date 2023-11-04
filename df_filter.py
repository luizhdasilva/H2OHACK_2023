import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import datetime
import numpy as np
from pandas.api.types import is_datetime64_any_dtype as is_datetime

def df_filter(data):
    # Try to convert to datetime, only if the column name has "date" in it
    # Will skip columns like "start_time" or "version"
    # for col in data.columns:
    #     if 'date' in col:
    #         for i in np.arange(data.shape[0]):
    #             data[col][i] = datetime.strptime(data[col][i],'%Y-%m-%d')

    # Add streamlit control gadgets 
    for col in data.columns:
        if is_datetime(data[col]):
            if data[col].isnull().any():
                continue
            user_date_input = st.date_input(
                f"Values for {col}",
                value=(
                    data[col].min(),
                    data[col].max(),
                ),
            )
            if len(user_date_input) == 2:
                user_date_input = tuple(map(pd.to_datetime, user_date_input))
                start_date, end_date = user_date_input
                data = data.loc[data[col].between(start_date, end_date)]

        # for now the main filtering function. The date filter is sometimes buggy
        elif (data[col].dtype != np.number) and ((data[col].nunique() < 30) and (data[col].nunique() > 1)):
            user_cat_input = st.sidebar.selectbox(
                f"Values for {col} ({data[col].nunique()} in total)",
                options=data[col].unique())
            st.session_state[col] = col
            data = data[data[col].isin([user_cat_input])]

    return data

def df_filter_container(data):
    modification_container = st.container()
    with modification_container:
        to_filter_columns = st.multiselect("Filter dataframe on", data.columns)
        for col in to_filter_columns:
            left, right = st.columns((1, 20))
            if isinstance(data[col].dtype, pd.CategoricalDtype) or ((data[col].nunique() < 30) and (data[col].nunique() > 1)):
                user_cat_input = right.multiselect(
                    f"Values for {col} ({data[col].nunique()} in total)",
                    data[col].unique(),
                    default=list(data[col].unique()),
                )
                
                data = data[data[col].isin(user_cat_input)]
    return data