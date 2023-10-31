# quickly test if git is working properly

import numpy as np
import pandas as pd
import os, sys 
from glob import glob 
import datetime as dt 
from pandas.api.types import is_datetime64_any_dtype as is_datetime


if __name__=='__main__':
    # flist = glob('./DATASET/*.csv')
    # for f in flist:
    #     df = pd.read_csv(f)
    #     print(df.columns)
    # df = pd.read_csv('./DATASET/IISD_ELA_Sites1,2,3_Lakes_Ref_Chem_2015_2020.csv')
    df = pd.read_csv('./DATASET/IISD_ELA_Sites1,2,3_Lakes_Ref_Secchi_2015_2020.csv')
    # print(df['characteristic_name'].dtype)
    # print(df['activity_media_name'].dtype)
    # df['activity_start_time'] = pd.to_datetime(df['activity_start_time'])
    for col in df.columns:
        if 'date' in col:
            try:
                df[col] = pd.to_datetime(df[col])
            except:
                pass 
    for col in df.columns:
        if is_datetime(df[col]):
            if df[col].isnull().any():
                print(col)
    # print(df['activity_start_time'].isnull().any())
    # print(pd.to_datetime(['1']))

    # print(df['activity_start_date'].dtype)
    # dt_obj = pd.to_datetime([dt.datetime(2000,1,1,1)])
    # print(dt_obj.dtype)
    # is_datetime(df['activity_start_date'])
    # # print(isinstance(df['activity_start_date'], ))
    # print(isinstance(df['characteristic_name'].dtype, object))