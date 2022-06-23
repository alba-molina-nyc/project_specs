import pandas as pd
import re
import itertools
from sqlalchemy import create_engine
from read_excel import read_mapping, read_ex_input

# ------------------------------------------------------------------------------------------------------------------------
# import xlsx files and save to database
# ------------------------------------------------------------------------------------------------------------------------

engine = create_engine('postgresql://albamolina@localhost/vidrio')

# df_ex_input.to_sql('Ex_input_file_02.04.2021.xlsx', con=engine)

# df_ex_mapping.to_sql('data/Ex_mapping_file.xlsx', con=engine)

