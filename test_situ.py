# quickly test if git is working properly

import numpy as np
import pandas as pd


if __name__=='__main__':
    df = pd.read_csv('./DATASET/IISD_ELA_Sites1,2,3_Lakes_Ref_Chem_2015_2020.csv')
    # df2 = pd.pivot(df, columns='characteristic_name')
    # print(df2.head())

    df2 = df[df['characteristic_name'].isin(['DIC','NO3'])]
    print(df2.head())
    # # Create a DataFrame in long format
    # df = pd.DataFrame({
    # 'team': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'],
    # 'player': [1, 2, 3, 4, 1, 2, 3, 4],
    # 'points': [11, 8, 10, 6, 12, 5, 9, 4]
    # })

    # # Pivot the DataFrame from long format to wide format
    # df = pd.pivot(df, columns='team')
    # print(df.head())