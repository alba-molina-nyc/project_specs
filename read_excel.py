import pandas as pd

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
    print(df_constituents.columns, 'before')
    df_constituents['NAV Change %'] = df_constituents['NAV % Change']
    print(df_constituents.columns, 'after')
    
    return df_constituents
read_c()

def read_id():
    df_index_data = pd.read_excel('data/Ex_input_file_02.04.2021.xlsx', 'Index Data')
    
    return df_index_data
read_id()
