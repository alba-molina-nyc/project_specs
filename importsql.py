import pandas as pd
from sqlalchemy import create_engine
from main import *

engine = create_engine('postgresql://albamolina@localhost/vidrio')
"""2. (Python) Read the ex_input file and save its content to database."""
df_ex_input = pd.read_excel('data/Ex_input_file_02.04.2021.xlsx')
# df_ex_input.to_sql('Ex_input_file_02.04.2021.xlsx', con=engine)
"""3. (Python) Read the mapping file and save its content to database."""
df_ex_mapping = pd.read_excel('data/Ex_mapping_file.xlsx')
# df_ex_mapping.to_sql('data/Ex_mapping_file.xlsx', con=engine)

# 4

# print(df_ex_input.columns, "=====> df ex col",
# df_ex_mapping.columns,  "=====> df ex mapping col",)

headers = df_ex_input.columns 


df_ex_input['Opening Allocation'] = df_ex_input['Beginning Weight %']

# Reference Day: taken from the time stamp portion of the input data file

df_ex_input['Reference Day'] = df_ex_input['LAST_UPDATE_DATE_EOD']
