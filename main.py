import re
import sys
from sqlalchemy import create_engine
import pandas as pd
sys.path
engine = create_engine('postgresql://albamolina@localhost/vidrio')

#1 extract the time stamp portion from the input file & display it in MM/DD/YYYY format
str = 'data/Ex_input_file_02.04.2021.xlsx'
match = re.match('(^[a-zA-Z_/]+)([0-9.]+)(.+$)',str)
buf= '/'.join(match.group(2)[:-1].split('.'))

#2 read data from input and mapping file and 
ifile_data = pd.read_excel('data/Ex_input_file_02.04.2021.xlsx')
mapping_data = pd.read_excel('data/Ex_mapping_file.xlsx')

#3 save data from input and mapping file and save it to database
ifile_data.to_sql('data/Ex_input_file_02.04.2021.xlsx', con=engine)
mapping_data.to_sql('data/Ex_mapping_file.xlsx', con=engine)

#4 generate portfolio valuation output file
temp_df = ifile_data.merge(mapping_data, how='left', right_on='Counterparty ID', left_on='ISIN ')
print(temp_df)