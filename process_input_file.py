import pandas as pd
from main import *
from importsql import *
import re

# ------------------------------------------------------------------------------------------------------------------------
# connect functins to connect to input in general, constituents, and index data 
# ------------------------------------------------------------------------------------------------------------------------

def connect():
    df_ex_input = pd.read_excel('data/Ex_input_file_02.04.2021.xlsx')
    return  df_ex_input
connect()

def connect_c():
    df_constituents = pd.read_excel('data/Ex_input_file_02.04.2021.xlsx', 'Constituents')
    return df_constituents
connect_c()

def connect_id():
    df_index_data = pd.read_excel('data/Ex_input_file_02.04.2021.xlsx', 'Index Data')
    return df_index_data
connect_id()

# ------------------------------------------------------------------------------------------------------------------------
# from  constituents keeps necessary ones 'LAST_UPDATE_DATE_EOD', 'Gross Contribution to Index', 'Net Contribution to Index', 'Beginning Weight %', 'End Weight %', '% Price Change'
# ------------------------------------------------------------------------------------------------------------------------
def drop_c_columns():
    df_constituents = connect_c()
    c_columns = df_constituents.drop(columns=['ISIN ', 'FUND_COMP_NAME', 'LONG_COMP_NAME', 'Strategy', 'Substrategy', 'Currency Denomination','Red Notice ', 'Red Settlement ', 'Sub Notice ', 'Sub Settlement ', 'Total Fund AUM','Beginning Weight $', 'End Weight $',
       'End Weight %', 'Trade_$_EoD', 'Attribution Gross $','Attribution Net $', 'Attribution Gross %', 'Attribution Net %',
       'Current Price', 'Current NAV', 'Previous Price', 'Previous NAV','% Price Change', 'Net Contribution to Index', 'PX_CLOSE_DT', 'FUND_TOTAL_ASSETS','FUND_TOTAL_ASSETS_DT', 'NAV % Change', 'BBG Total Return'])
    return c_columns

drop_c_columns()

def drop_id_columns():
    df_index_data = connect_id()
    id_columns = df_index_data.drop(columns=['Date', 'Total AUM',  'Previous Day NAV', 'NAV Change $',  'NAV Change %','AUM Change from Previous Day', 'Previous Day AUM'])
    return id_columns
    
drop_id_columns()

    
    

# headers = df_input_file.columns 
# print(headers)

# kee= 'ISIN ' (B) 'Index Name' (c)
