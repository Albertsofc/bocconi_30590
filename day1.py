# import pandas as pd
# data =  pd.read_csv('bridges.data', sep=",")
# print(data) 
#print(data) 
import csv


def nth_line(filename, nline):
    with open(filename, 'r') as f:
        x = f.readlines()[nline:nline+1]
        print(x)
    # to avoid unicode decode error: (important if you're working with text files)
        # with open(filename, 'r', encoding = 'utf-8') as f:
        #     counter = 0
        #     for counter, line in enumerate(f):
        #         if counter == nline-1:
        #             return line
        

def bridges_per_year(filename, year_field_name):
    # returns a dictionary with the years of construction 
    # as keys and the number of bridges built in that year 
    # as the corresponding value. For example, d[1818]=1
    with open(filename, 'r') as f:
        linereader = csv.DictReader(f, delimiter=",")
        for row in linereader:
            # # solution 1
            # d[row[year_field_name]] = d.get(row[year_field_name], 0) + 1
            # # # notes on .get(key)
            # # .get(key) --> returns the key's value
            # # .get(key, other_value) --> returns the key's value, or 
            # # returns the other_value. So for line 22, the chunk of code
            # # d.get(row[year_field_name], 0)
            # # returns 0 if the key doesn't already exist
            # # solution 2
            # if row[year_field_name] in d:
            #     d[row[year_field_name]] +=1
            # else:
            #     d[row[year_field_name]] = 1
            # # prof's solution
            bridges_per_year = {}
            with open(filename, 'r') as fp:
                dict_reader = csv.DictReader(fp, delimiter=',')
                for row in dict_reader:
                    year = int(row[year_field_name])
                    if year in bridges_per_year.keys():
                        bridges_per_year[year] += 1
                    else:
                        bridges_per_year[year] = 1
                        
    return bridges_per_year  
    # # general inversion
    # def invert_dict(d):
    #     inverse = dict()
    #     for key in d.keys():
    #         val = d[key]
    #         if val not in inverse:
    #             inverse[val] = key
    #         else:
    #             inverse[val].append(key)
    #     return inverse


def year_per_number_of_bridges(filename, year_field_name):
    # returns a dictionary with the number of bridges built as 
    # keys and a list of the years during which those bridges
    # were built as the corresponding value. 
    # For example, d[4]=[1903, 1927, 1928]
    bpy_dict = bridges_per_year(filename, year_field_name)
    year_per_num_bridges = {}
    for year in bpy_dict.keys():
        num_bridges = bpy_dict.get(year)
        if num_bridges in year_per_num_bridges.keys():
            year_per_num_bridges[num_bridges].append(year)
        else:
            year_per_num_bridges[num_bridges] = [year]
    return year_per_num_bridges




def materials(filename, material_field_name, unknown_key):
    # returns a dictionary with the construction materials of
    # the bridges as keys and the number of bridges built with
    # that material as the corresponding value. For example, 
    # d['IRON']=11. For unknown material, the key should
    # be the string unknown_key
    with open(filename, 'r') as f:
        linereader = csv.DictReader(f, delimiter=",")
        for row in linereader:
            materials = {}
            with open(filename, 'r') as fp:
                dict_reader = csv.DictReader(fp, delimiter=',')
                for row in dict_reader:
                    material = row[material_field_name]
                    if material == '?':
                        material = unknown_key
                    if material in materials.keys():
                        materials[material] += 1
                    else:
                        materials[material] = 1
                    
    return materials


filename = 'bridges.data'
nline = 3
#nth_line(filename, nline)
# print(bridges_per_year('bridges.data', "ERECTED"))
print(year_per_number_of_bridges('bridges.data', "ERECTED"))
# print(materials('bridges.data', "MATERIAL", "unknown material"))
