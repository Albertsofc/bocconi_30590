# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 10:33:06 2020

@author: Iozzi

NOTES:
    write (w) will over-write, append (a) will append
    writing will totally delete the file and insert whatever you've added'
"""

import random

out_filename = 'numbers.txt'

# with open(out_filename,'w', encoding='utf-8') as file_out:
#     for i in range(5):
#         rn = random.randint(1,100)
#         line_to_write = str(rn) + '\n'
#         file_out.writelines(line_to_write)

# with open(out_filename,'a') as file_out:
#     for i in range(5):
#         rn = random.randint(1,100)
#         line_to_write = str(rn) + '\n'
#         file_out.writelines(line_to_write)

in_filename = 'numbers.txt'
out_filename = 'smallnumbers.txt'
threshold = 50

with open(in_filename,'r') as f_in, open(out_filename,'w') as f_out:
    for line in f_in:
        if int(line) < threshold:
            f_out.writelines(line)
