import pandas as pd
from sqlalchemy import create_engine
from main import *
import re

# ------------------------------------------------------------------------------------------------------------------------
# Connect to SQL, read excel files, read diff tabs in file
# ------------------------------------------------------------------------------------------------------------------------
engine = create_engine('postgresql://albamolina@localhost/vidrio')
df_input_file = df_ex_input = pd.read_excel('data/Ex_input_file_02.04.2021.xlsx')
df_constituents = pd.read_excel('data/Ex_input_file_02.04.2021.xlsx', 'Constituents')
df_index_data = pd.read_excel('data/Ex_input_file_02.04.2021.xlsx', 'Index Data')
# df_ex_input.to_sql('Ex_input_file_02.04.2021.xlsx', con=engine)
df_ex_mapping = pd.read_excel('data/Ex_mapping_file.xlsx')
# df_ex_mapping.to_sql('data/Ex_mapping_file.xlsx', con=engine)

# ------------------------------------------------------------------------------------------------------------------------
# Q4 
# ------------------------------------------------------------------------------------------------------------------------
headers = df_input_file.columns 
df_input_file['Reference Day'] = df_input_file['LAST_UPDATE_DATE_EOD']
df_input_file['Opening Allocation'] = df_input_file['Beginning Weight %']
nn = [i for i in df_index_data['ISIN '] if i == 'HFRIILAU']





for index, row in df_index_data.iterrows():
    for i, r in df_input_file.iterrows():
        # print(index, row, i, r)
    x = ''
    if df_index_data['ISIN '].item() == 'HFRIILAU':
        x = df_input_file['Investor Account Long Name']
        # print(x)
        break
    
      
# xx = [i for i in df_index_data['Index Name'] if i == 'HFRIILAU' and i == df_input_file['Reference Day'] ]
# print(xx)
# df_input_file['Investor Account Long Name'] = df_index_data['Index Name']
# print(df_input_file['Investor Account Long Name'], 'here')