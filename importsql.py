import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://albamolina@localhost/vidrio')
print(engine)
df = pd.read_excel('data/Ex_input_file_02.04.2021.xlsx')
print(df)

df.to_sql('ex_input', con=engine)


