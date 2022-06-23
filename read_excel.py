import pandas as pd
from change_filename import * 

# ------------------------------------------------------------------------------------------------------------------------
# read functins to read the input in general, constituents, index data & the mapping file
# ------------------------------------------------------------------------------------------------------------------------
def read_mapping():
    df_ex_mapping = pd.read_excel('data/Ex_mapping_file.xlsx')
  
    return df_ex_mapping
read_mapping()

def read_ex_input():
    df_ex_input = pd.read_excel('data/Ex_input_file_02.04.2021.xlsx')
   
    return  df_ex_input
read_ex_input()

def read_c():
    df_constituents = pd.read_excel('data/Ex_input_file_02.04.2021.xlsx', 'Constituents')
    df_constituents['NAV Change %'] = df_constituents['NAV % Change']
    return df_constituents
read_c()

def read_id():
    df_index_data = pd.read_excel('data/Ex_input_file_02.04.2021.xlsx', 'Index Data')
    return df_index_data
read_id()

def merge_all():
    df_index_data = read_id()
    df_constituents = read_c()

    all_columns_merged = df_index_data[['Date', 'ISIN ', 'Index Name', 'Total AUM', 'Previous Day AUM',
       'AUM Change from Previous Day', 'NAV', 'Previous Day NAV', 'NAV Change $', 'NAV Change %']].merge(df_constituents[['Date', 'ISIN ', 'FUND_COMP_NAME', 'LONG_COMP_NAME', 'Strategy', 'Substrategy', 'Currency Denomination', 'Red Notice ', 'Red Settlement ', 'Sub Notice ', 'Sub Settlement ', 'Total Fund AUM', 'Beginning Weight $', 'Beginning Weight %', 'End Weight $', 'End Weight %', 'Trade_$_EoD', 'Attribution Gross $', 'Attribution Net $', 'Attribution Gross %', 'Attribution Net %', 'Current Price', 'Current NAV', 'Previous Price', 'Previous NAV','% Price Change', 'Gross Contribution to Index', 'Net Contribution to Index', 'PX_CLOSE_DT', 'FUND_TOTAL_ASSETS', 'FUND_TOTAL_ASSETS_DT', 'NAV % Change', 'BBG Total Return', 'LAST_UPDATE_DATE_EOD', 'CHECK_DATE', 'NAV Change %']], on='NAV Change %', how = 'right')
    print(all_columns_merged.columns)

    


merge_all()



#  df_index_data['Date '] = df_constituents['']
#     x = df_index_data.loc[df_index_data['ISIN '] == 'HFRIILAU']
    
#     print(x, 'x')
   