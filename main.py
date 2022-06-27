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
ifile_data = pd.read_excel('data/Ex_input_file_02.04.2021.xlsx', sheet_name=['Constituents', 'Index Data'])
constitutents = ifile_data['Constituents']
index = ifile_data['Index Data']
ifile_data = constitutents.merge(index, how='outer', right_on='Index Name', left_on='ISIN ')
ifile = pd.concat([constitutents, index])



print(len(ifile_data), 'ifiledata col')
print(ifile_data.columns)
ifile = pd.concat([constitutents, index])
print(len(ifile))
print(ifile['ISIN '])

mapping_data = pd.read_excel('data/Ex_mapping_file.xlsx')

#3 save data from input and mapping file and save it to database
# ifile_data.to_sql('data/Ex_input_file_02.04.2021.xlsx', con=engine)
# mapping_data.to_sql('data/Ex_mapping_file.xlsx', con=engine)

#4 generate portfolio valuation output file
temp_df = ifile.merge(mapping_data, how='left', right_on='Counterparty ID', left_on='ISIN ')
print(len(ifile.columns), 'ifile col')
print(len(mapping_data.columns), 'mappcol')

# print(mapping_data.columns, 'map cols has counterparty id')
print(len(temp_df.columns))

for col in temp_df.columns:
    temp_df['Reference Day'] = temp_df['LAST_UPDATE_DATE_EOD']
    temp_df['Periodicity'] = 'Daily'
    temp_df['Attribution Gross'] = temp_df['Gross Contribution to Index']
    temp_df['Attribution Net'] = temp_df['Net Contribution to Index']
    temp_df['Opening Allocation'] = temp_df['End Weight %']
    temp_df['Closing Allocation'] = temp_df['End Weight %']
    temp_df['Investment Performance'] = temp_df['% Price Change']
    # print(temp_df)
    # print(temp_df.columns)
    break