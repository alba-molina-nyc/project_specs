from ast import parse
import re
import sys
from sqlalchemy import DDL, create_engine
import pandas as pd
sys.path
import datetime

engine = create_engine('postgresql://albamolina@localhost/vidrio')

#1 extract the time stamp portion from the input file & display it in MM/DD/YYYY format
str = 'data/Ex_input_file_02.04.2021.xlsx'
match = re.match('(^[a-zA-Z_/]+)([0-9.]+)(.+$)',str)
buf= '/'.join(match.group(2)[:-1].split('.'))

#2 read data from input and mapping file and 
ifile_data = pd.read_excel('data/Ex_input_file_02.04.2021.xlsx', sheet_name=['Constituents', 'Index Data'], parse_dates=True)
constitutents = (ifile_data['Constituents'])
index = ifile_data['Index Data']
# print(index.columns)
# print(index['Previous Day NAV'])


ifile_data = constitutents.merge(index, how='outer', right_on='Index Name', left_on='ISIN ')
ifile = pd.concat([constitutents, index])
mapping_data = pd.read_excel('data/Ex_mapping_file.xlsx', parse_dates=True)
#3 save data from input and mapping file and save it to database
# ifile_data.to_sql('data/Ex_input_file_02.04.2021.xlsx', con=engine)
# mapping_data.to_sql('data/Ex_mapping_file.xlsx', con=engine)

#4 generate portfolio valuation output file
temp_df = ifile.merge(mapping_data, how='left', right_on='Counterparty ID', left_on='ISIN ')


for col in temp_df.columns:
    temp_df['Reference Day'] = temp_df['LAST_UPDATE_DATE_EOD']
    temp_df['Periodicity'] = 'Daily'
    temp_df['Investor Account UID'] = temp_df['ISIN '] == 'HFRIILAU' 
    #TODO figure out how to useregex to change the date format
    # temp_df['Investor Account Long Name'] = (temp_df['ISIN '] == 'HFRIILAU') & (temp_df['Date'] == (temp_df['Reference Day']))   
    temp_df['Investment Account UID'] = ' '
    # temp_df['Investment Account Long Name'] = temp_df['']                     #TODO: come back         
    temp_df['Attribution Gross'] = temp_df['Gross Contribution to Index']
    temp_df['Attribution Net'] = temp_df['Net Contribution to Index']
    temp_df['Opening Allocation'] = temp_df['End Weight %']
    temp_df['Closing Allocation'] = temp_df['End Weight %']
    #TODO figure out how to useregex to change the date format OR figure out how to use datetime
    # temp_df['Opening Equity'] = (temp_df['Index Name'] == 'HFRI-I Liquid Alt UCITS Index\n(Net)') & (temp_df['Date'] == temp_df['Reference Day'])            
    #TODO: figure out how to useregex to change the date format OR figure out how to use datetime                   
    # temp_df['Closing Equity'] = (temp_df['NAV'] == temp_df['Index Name'] == 'HFRI-I Liquid Alt UCITS Index\n(Net)') & (temp_df['Date'] == temp_df['Reference Day'])           
    temp_df['Investment Performance'] = temp_df['% Price Change']
    # temp_df['Investment Adj Opening Balance'] = temp_df['']         #TODO: come back
    # temp_df['Investment Closing Balance'] = temp_df['']             #TODO: come back
    # temp_df['Portfolio Opening Balance'] = temp_df['']              #TODO: come back
    # temp_df['Portfolio Closing Balance'] = temp_df['']              #TODO: come back
    break


# print(temp_df.columns)
#     counter = 0
#     for col in temp_df.columns:
#         print(col)
#         counter += 1
#         print(counter, col)
#         continue

# start pi
# y = temp_df.loc[temp_df['Date'].str.contains('^-[a-z]*', regex=True)]
# print(y,'y')
# print(temp_df['Date'] )
# ('^pi[a-z]')