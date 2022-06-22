import pandas as pd
from main import *
from importsql import *
import re



def connect():
    df_ex_input = pd.read_excel('data/Ex_input_file_02.04.2021.xlsx')
    # print( df_ex_input)
    return  df_ex_input
connect()

# ------------------------------------------------------------------------------------------------------------------------
# from  constituents keeps necessary ones 'LAST_UPDATE_DATE_EOD', 'Gross Contribution to Index', 'Net Contribution to Index', 'Beginning Weight %', 'End Weight %', '% Price Change'
# ------------------------------------------------------------------------------------------------------------------------
def drop_columns():
    df_ex_input = connect()
    columns = df_ex_input.drop(columns=['ISIN ', 'FUND_COMP_NAME', 'LONG_COMP_NAME', 'Strategy', 'Substrategy', 'Currency Denomination','Red Notice ', 'Red Settlement ', 'Sub Notice ', 'Sub Settlement ', 'Total Fund AUM','Beginning Weight $', 'End Weight $',
       'End Weight %', 'Trade_$_EoD', 'Attribution Gross $','Attribution Net $', 'Attribution Gross %', 'Attribution Net %',
       'Current Price', 'Current NAV', 'Previous Price', 'Previous NAV','% Price Change', 'Net Contribution to Index', 'PX_CLOSE_DT', 'FUND_TOTAL_ASSETS','FUND_TOTAL_ASSETS_DT', 'NAV % Change', 'BBG Total Return'])
    print(columns, 'here')
    return columns

drop_columns()
    
    

headers = df_input_file.columns 
print(headers)

# print(df_input_file['Reference Day'], '1')
# print(df_input_file['Opening Allocation'], '2')
# print(df_input_file['Attribution Gross'], '3')
# print(df_input_file['Attribution Net'], '4')
# print(df_input_file['Opening Allocation'] ,' 5 ')
# print(df_input_file['Closing Allocation'],'6')
# print(df_input_file['Investment Performance'] ,'7')



# df_input_file['Reference Day'] = df_input_file['LAST_UPDATE_DATE_EOD']
#     df_input_file['Opening Allocation'] = df_input_file['Beginning Weight %']
#     df_input_file['Attribution Gross'] = df_input_file['Gross Contribution to Index']
#     df_input_file['Attribution Net'] = df_input_file['Net Contribution to Index']
#     df_input_file['Opening Allocation'] = df_input_file['Beginning Weight %']
#     df_input_file['Closing Allocation'] = df_input_file['End Weight %']    
#     df_input_file['Investment Performance'] = df_input_file['% Price Change']  


# df_input_file['Reference Day'] = df_input_file['LAST_UPDATE_DATE_EOD'], df_input_file['Opening Allocation'] = df_input_file['Beginning Weight %'],df_input_file['Attribution Gross'] = df_input_file['Gross Contribution to Index'], df_input_file['Attribution Net'] = df_input_file['Net Contribution to Index'], df_input_file['Opening Allocation'] = df_input_file['Beginning Weight %'],df_input_file['Closing Allocation'] = df_input_file['End Weight %'],df_input_file['Investment Performance'] = df_input_file['% Price Change']  

# keeping:  'LAST_UPDATE_DATE_EOD', 'Gross Contribution to Index', 'Net Contribution to Index', 'Beginning Weight %', 'End Weight %', '% Price Change'