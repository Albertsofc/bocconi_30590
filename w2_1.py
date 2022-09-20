# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# def nth_line(filename, nline, encoding):
#     with open(filename, 'r', encoding=encoding) as f:
def nth_line(filename, nline):
    with open(filename, 'r', encoding = 'utf-8') as f:
        # daniel proposal
        # doc = f.read()
        # doc = doc.split('\n')
        # print(doc[nline - 1])
        counter = 0
        for counter, line in enumerate(f):
            if counter == nline-1:
                return line

if __name__ == '__main__':
    filename = 'Artists.txt'
    nline = 300
    # print(nth_line(filename, nline, 'utf-8'))
    print(nth_line(filename, nline))
