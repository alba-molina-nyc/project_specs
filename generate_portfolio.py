import pandas as pd
from read_excel import *
from importsql import *

def get_c_cols():
    df_constituents_data = read_c()
    df_constituents_data = df_constituents_data.drop(columns=[ 'FUND_COMP_NAME', 'LONG_COMP_NAME', 'Strategy', 'Substrategy', 'Currency Denomination', 'Red Notice ', 'Red Settlement ', 'Sub Notice ', 'Sub Settlement ', 'Total Fund AUM','Beginning Weight $', 'End Weight $', 'Trade_$_EoD', 'Attribution Gross $','Attribution Net $', 'Attribution Gross %', 'Attribution Net %', 'Current Price', 'Current NAV', 'Previous Price', 'Previous NAV', 'PX_CLOSE_DT', 'FUND_TOTAL_ASSETS','FUND_TOTAL_ASSETS_DT', 'NAV % Change', 'BBG Total Return'])
    df_constituents_data.columns
    print(df_constituents_data.columns, 'this is the const columns')
    return df_constituents_data
get_c_cols()

def get_i_cols():
    df_index_data = read_id()  
    df_index_data = df_index_data.drop(columns=['Total AUM', 'NAV Change $', 'AUM Change from Previous Day','Previous Day AUM' ])
    df_index_data.columns
    print(df_index_data.columns, 'this is the index columns')
    return df_index_data

get_i_cols()

def get_m_cols():
    df_ex_mapping = read_mapping()
    cols = list(df_ex_mapping.columns)
    # print(cols, 'mapp#######ing')
    return cols

get_m_cols()