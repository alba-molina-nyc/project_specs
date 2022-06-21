import pandas as pd
from sqlalchemy import create_engine
from main import *

engine = create_engine('postgresql://albamolina@localhost/vidrio')

df = pd.read_excel('data/Ex_input_file_02.04.2021.xlsx')

df.to_sql('Ex_input_file_02.04.2021.xlsx', con=engine)
