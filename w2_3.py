# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 10:43:12 2020

@author: Iozzi
"""

import csv

def bridges_purpose(file_in, purpose_field_name, purpose, file_out):
    with open(file_in,'r') as f_in, open(file_out,'w', newline='') as f_out:
        dict_reader = csv.DictReader(f_in, delimiter=',')
        # this is important - list of all the fields
        fieldnames = dict_reader.fieldnames
        dict_writer = csv.DictWriter(f_out, fieldnames)
        dict_writer.writeheader()
        for row in dict_reader:
            if row[purpose_field_name] == purpose:
                dict_writer.writerow(row)

if __name__ == '__main__':
    bridges_purpose('bridges.data', 'PURPOSE', 'HIGHWAY', 'highway_bridges.csv')