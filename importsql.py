import pandas as pd
from sqlalchemy import create_engine
from main import *

engine = create_engine('postgresql://albamolina@localhost/vidrio')

df_ex_input = pd.read_excel('data/Ex_input_file_02.04.2021.xlsx')

df_ex_input.to_sql('Ex_input_file_02.04.2021.xlsx', con=engine)



"""3. (Python) Read the mapping file and save its content to database."""

df_ex_mapping = pd.read_excel('data/Ex_mapping_file.xlsx')
df_ex_mapping.to_sql('data/Ex_mapping_file.xlsx', con=engine)

