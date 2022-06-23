import pandas as pd 
from datetime import datetime, date
import os
path = '/Users/albamolina/take1/data'

"""# 1 (Python) Extract a time stamp portion from the input file name and display it in MM/DD/YYYY format when"""

def change_filename():
    date_form_list = []
    for input_file in os.listdir(path):
        filename = input_file[0:-5]
        for i in filename:
            if i in '0123456789':
                date_form_list.append(i)
            else:
                if i in '.':
                    i = '/'
                    date_form_list.append(i)
        date_str_form = ''.join(str(i) for i in date_form_list)
        filename = date_str_form + '.xlsx'
    print('this is the new filename: ', filename)
    return filename
    
change_filename()

