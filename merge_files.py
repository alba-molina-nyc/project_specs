from operator import index
import pandas as pd
from read_excel import *
from importsql import *
from generate_portfolio import *
from change_filename import *


# merge files on 'NAV Change % 


def merge_files():
    index_file = get_c_cols()
    constituents_file = get_i_cols()
    merged_file = index_file.merge(constituents_file[['Date', 'ISIN ', 'Index Name', 'NAV', 'Previous Day NAV',
       'NAV Change %']], on='NAV Change %', how = 'left')
    return merged_file

merge_files()