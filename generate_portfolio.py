import pandas as pd
from read_excel import *
from importsql import *
from merge_files import *
from change_filename import * 

def generate_portfolio():
    portfolio = merge_files()
    portfolio['Reference Day'] = portfolio['LAST_UPDATE_DATE_EOD']
    print(portfolio)
    print(portfolio.columns)


generate_portfolio()

# LAST_UPDATE_DATE_EOD - now you can get rid of last update end of day