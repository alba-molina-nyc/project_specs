import pandas as pd 
from datetime import datetime, date
import os
path = '/Users/albamolina/take1/data'
# input_file = pd.read_excel('Ex_input_file_02.04.2021.xlsx', index_col=0, header=0)
# print(input_file)

# 1. (Python) Extract a time stamp portion from the input file name and display it in MM/DD/YYYY format when


def get_date():
    date_form_list = []
    for input_file in os.listdir(path):
        date_holder = input_file[14:24:1]
        print(date_holder, 'we are here')
        for i in date_holder:
            if i in '0123456789':
                date_form_list.append(i)
            else:
                if i in '.':
                    i = '/'
                    date_form_list.append(i)
    
    print(date_form_list, 'dateholder')
    print(''.join(str(i) for i in date_form_list), 'joinerjoiner')
    return ''.join(str(i) for i in date_form_list)
                
get_date()

# def change_filename():




# def change_input_filename():
#     input_file_list = []
#     for input_file in os.listdir(path):
#         if input_file.endswith('.xlsx'):
#             input_date = slice(14, 24, 1)
#             new_date = input_file[input_date].strptime(input_date, "%Y-%m-%d %H:%M:%S.%f" )
#             # new_date = input_date.strftime(input_date, "%Y-%m-%d" )
#             print(input_file[input_date], 'we are here')
#             print(new_date)
#             print(input_date, 'input date')
#             # new_date = input_date.strftime("%Y-%m-%d")
#             # print(new_date, new_date)
         
#             # filename = input_file[:14]
#             # print(filename, 'filename')
#             # print(input_file)
#             # print(input_file_list)

# change_input_filename()

# print(input_file.columns)