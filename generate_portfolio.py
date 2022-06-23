import pandas as pd
from read_excel import *
from importsql import *
from merge_files import *
from change_filename import * 

def generate_portfolio():
    portfolio = merge_files()
    print(portfolio)
    print(portfolio.columns)


generate_portfolio()