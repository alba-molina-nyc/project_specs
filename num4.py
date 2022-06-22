import pandas as pd
from sqlalchemy import create_engine
from main import *
import re

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
# Question 4 TODO: change the file name once figured out logic DAV Proforma ACC Analy.xlsx['Reference Day'] = df_ex_input['LAST_UPDATE_DATE_EOD'] and insert the columns in there
# ------------------------------------------------------------------------------------------------------------------------
headers = df_input_file.columns 
# print(headers)
df_input_file['Reference Day'] = df_input_file['LAST_UPDATE_DATE_EOD']
# print(df_input_file['Reference Day'])
df_input_file['Opening Allocation'] = df_input_file['Beginning Weight %']
# print(df_input_file['Opening Allocation'])
nn = [i for i in df_index_data['ISIN '] if i == 'HFRIILAU']
print(nn)
# TODO: figure out how to set nn values equal to df_input_file['Investor Account UID']
# df_input_file['Investor Account UID'] == nn
df_input_file['Investor Account Long Name'] = ''
df_input_file['Investment Account UID'] = ''
df_input_file['Investment Account Long Name'] = ''
df_input_file['Attribution Gross'] = ''
df_input_file['Attribution Net'] = ''
df_input_file['Opening Allocation'] = ''
df_input_file['Closing Allocation'] = ''
df_input_file['Opening Equity'] = ''
df_input_file['Closing Equity'] = ''
df_input_file['Investment Performance'] = ''
df_input_file['Investment Adj Opening Balance'] = ''
df_input_file['Investment Closing Balance'] = ''
df_input_file['Portfolio Opening Balance'] = ''
df_input_file['Portfolio Closing Balance:'] = ''











# def get_account_uid():
#     # df_input_file['Investor Account UID'] = []
#     for index, row in df_index_data.iterrows():
#         while row['ISIN '] != None:
#             if row['ISIN '] == 'HFRIILAU':
#                 df_input_file['Investor Account UID'].append(row['ISIN '])
#                 # print(x)
#                 # break
           
                

#     return df_input_file['Investor Account UID'] 
               
        
# get_account_uid()
# # print(get_account_uid())
# df_input_file['Investor Account UID'] = get_account_uid()
# print(df_input_file['Investor Account UID'])




# x = df_input_file['Investor Account UID'] 

# print(df_input_file['Investor Account UID'])


  
      






# df_input_file['Investor Account UID'] = [(index, row) for index, row in df_index_data.iterrows() if (index,row['ISIN '])]
# print(df_input_file['Investor Account UID'])
# df_input_file['Investor Account UID'] = [i for i in df_index_data['ISIN '] if i == 'HFRIILAU']
# print(df_input_file['Investor Account UID'])

# df_input_file['Investor Account UID'] = df_index_data['ISIN ']
# print(df_input_file['Investor Account UID'])

"""
(Python) Using “pandas” package to generate portfolio valuation output file
(“DAV Proforma Acc Analy.xlsx”) that will have the following columns (col names in bold, specs below):

Reference Day: taken from the time stamp portion of the input data file
Periodicity: ‘Daily’

Investor Account UID: “HFRIILAU” from column B in the “Index Data” tab of the input data file

Investor Account Long Name: From column C in the “Index Data” tab of the input data file where ISIN =
“HFRIILAU” and Date= Reference Day
Investment Account UID: Leave blank
Investment Account Long Name: Have to translate company name from “Constituents” tab of the data
input file to Product Name from the mapping file using “ISIN” column from the “Constituents” tab and
“Counterparty ID” column in the mapping file as matching keys. Use these keys to match all records in
the output data set.
Attribution Gross: “Gross Contribution to Index” column from “Constituents” tab
Attribution Net: “Net Contribution to Index” column from “Constituents” tab
Opening Allocation: 'Beginning Weight %' column from “Constituents” tab
Closing Allocation: 'End Weight %' column from “Constituents” tab
Opening Equity: ‘Previous Day NAV’ column from Index Data tab for ‘HFRI-I Liquid Alt UCITS Index’ index
for Reference Day
Closing Equity: ‘NAV’ column from Index Data tab for ‘HFRI-I Liquid Alt UCITS Index’ index for Reference
Day
Investment Performance: '% Price Change' column from “Constituents” tab
Investment Adj Opening Balance: 'Opening Allocation' * 'Opening Equity'
Investment Closing Balance: 'Closing Allocation' * 'Closing Equity'
Portfolio Opening Balance: 'Investment Adj Opening Balance'"""


# 4
# print(df_ex_input.columns, "=====> df ex col",
# df_ex_mapping.columns,  "=====> df ex mapping col",)





for index, row in df_ex_input.iterrows():
    # print(index,row['Current NAV'])
    break

#for accessing only particular rows use .loc
y = df_ex_input.loc[df_ex_input['Current Price'] == 14.71]
# print(y, 'y')

# TODO: figure out how to do multiple conditions


# add a column called investment closing balance = closing allocation * closing equity 

# df_ex_input['investment_closing_balance'] = df_ex_input['closing']

# Opening Allocation: 'Beginning Weight %' column from “Constituents” tab 








# print(df_ex_input['Opening Allocation'])

# print(df_index_data)
# print(df_ex_input.columns)



# 4

# print(df_ex_input.columns, "=====> df ex col",
# df_ex_mapping.columns,  "=====> df ex mapping col",)

# headers = df_ex_input.columns 


# df_ex_input['Opening Allocation'] = df_ex_input['Beginning Weight %']

# # Reference Day: taken from the time stamp portion of the input data file

# df_ex_input['Reference Day'] = df_ex_input['LAST_UPDATE_DATE_EOD']

# # Periodicity: ‘Daily’
# df_ex_input['Periodicity'] = 'Daily'

# # Investor Account UID: “HFRIILAU” from column B in the “Index Data” tab of the input data file 

# headers = df_ex_input.columns 
# print(headers )

# df_ex_input['Investor Account UID'] = 

# # df_ex_input['name_of_column'] = df_ex_input['LAST_UPDATE_DATE_EOD']

# # headers = df_ex_input.columns 