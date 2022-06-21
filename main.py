import pandas as pd 
from datetime import date, datetime

print(datetime.now())

# print(pd.__version__)

pd.read_excel('Ex_input_file_02.04.2021.xlsx', index_col=0, header=0)

# print(pd.read_excel('Ex_input_file_02.04.2021.xlsx', index_col=0, header=0))