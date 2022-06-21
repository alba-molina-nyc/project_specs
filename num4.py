import pandas as pd
from sqlalchemy import create_engine
from main import *

engine = create_engine('postgresql://albamolina@localhost/vidrio')
df_ex_input = pd.read_excel('data/Ex_input_file_02.04.2021.xlsx')
df_ex_mapping = pd.read_excel('data/Ex_mapping_file.xlsx')



x = change_filename()
for i in x:
    reference_day = x[14:24:1]
    break

print(reference_day, )
    



# print(df_ex_input.columns, "=====> df ex col")


# print(df_ex_mapping.columns,  "=====> df ex mapping col")