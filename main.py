import pandas as pd 
from datetime import datetime, date
import os
path = '/Users/albamolina/take1/data'

"""
# 1 (Python) Extract a time stamp portion from the input file name and display it in MM/DD/YYYY format when
"""

def get_date():
    date_form_list = []
    for input_file in os.listdir(path):
        input_time_stamp = input_file[14:24:1]
        for i in input_time_stamp:
            if i in '0123456789':
                date_form_list.append(i)
            else:
                if i in '.':
                    i = '/'
                    date_form_list.append(i)
        date_str_form = ''.join(str(i) for i in date_form_list)
        filename = input_file[:14] + date_str_form
    print(filename)
    return filename
                
get_date()

"""
--------------------------------------------------------------------------------------------------------------
NOTE: assumptions I am making in my above get_date():
1. I am assuming that I will always find the time stamp at the slicing done in input_time_stamp, what if the date appears at the beginning? (The reason I did it that way is because there is a trailing '.' at the end of the filename for the '.xlsx' 
- so this is an edge case I would further consider if I was not pressed for time 
i.e. - 

if i in '.' and i.next not in '0123456789' => then i would not append to the list 
but if i in '.' and i.next in '0123456789' -> then yes append to the list )
--------------------------------------------------------------------------------------------------------------
"""



