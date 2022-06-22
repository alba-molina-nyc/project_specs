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


"""NOTE about step 2 and step 3 
1. This "gets the job done through "brute force"  but I want to refactor this tomorrow morning to have it be a for loop with a list of nested dictionaries instead for the files, this way the forloop can unpack those dictionaries
2. I want to also make the pd.read_excel() method table naming dynamic - 
- I also think this can come together with the for loop/unpacking the list of dicts
3. Furthermore, to build on step 2- I will make it dynamic based on the renaming of the file to fit the format that step 1 asks 
"""

# 4

# print(df_ex_input.columns, "=====> df ex col",
# df_ex_mapping.columns,  "=====> df ex mapping col",)

headers = df_ex_input.columns 

reference_day = df_ex_input['LAST_UPDATE_DATE_EOD']
print(reference_day)

"""
Reference Day: taken from the time stamp portion of the input data file 
bc last time they put it in """