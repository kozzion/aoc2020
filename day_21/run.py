import os
import sys
import copy
import numpy as np
from scipy import ndimage

with open('input.txt', 'r') as file:
    list_line = file.readlines()
list_line = [line.strip() for line in list_line]

#parse
list_dish = []
for line in list_line:
    dish = {}
    dish['list_ingredient'] = line.split(' (contains ')[0].split(' ')
    dish['list_allergen'] = line.split(' (contains ')[1][:-1].split(', ')
    list_dish.append(dish)

dict_ingredient = {}
for dish in list_dish:
    for ingredient in dish['list_ingredient']:
        if not ingredient in dict_ingredient:
            dict_ingredient[ingredient] = True
list_ingredient = list(dict_ingredient.keys())

dict_allergen_to_list_ingredient_possible = {}
for dish in list_dish:
    for allergen in dish['list_allergen']:
        if not allergen in dict_allergen_to_list_ingredient_possible:
            dict_allergen_to_list_ingredient_possible[allergen] = copy.copy(dish['list_ingredient'])

        else:
            list_ingredient_possible = dict_allergen_to_list_ingredient_possible[allergen]
            for ingredient in list_ingredient:
                if ingredient in list_ingredient_possible:
                    if not ingredient in dish['list_ingredient']:
                        list_ingredient_possible.remove(ingredient)








#part_1
list_ingredient_clean = copy.copy(list_ingredient)
for allergen, list_ingredient_possible in dict_allergen_to_list_ingredient_possible.items():
    for ingredient in list_ingredient_possible:
        if ingredient in list_ingredient_clean:
            list_ingredient_clean.remove(ingredient)

count = 0
for dish in list_dish:
    for ingredient in dish['list_ingredient']:
        if ingredient in list_ingredient_clean:
            count += 1

print(count)



dict_allergen = {}
count_found = 1
while 0 < count_found:
    count_found = 0
    for allergen, ingredient in dict_allergen.items():
        if allergen in dict_allergen_to_list_ingredient_possible:
            del dict_allergen_to_list_ingredient_possible[allergen]
        for allergen in dict_allergen_to_list_ingredient_possible:

            if ingredient in dict_allergen_to_list_ingredient_possible[allergen]:
                dict_allergen_to_list_ingredient_possible[allergen].remove(ingredient)
    for allergen, list_ingredient_possible in dict_allergen_to_list_ingredient_possible.items():
        if len(list_ingredient_possible) == 1:
            dict_allergen[allergen] = list_ingredient_possible[0]
            count_found += 1

str_list = ''
for allergen in sorted(list(dict_allergen.keys())):
    str_list += ',' + dict_allergen[allergen]
str_list = str_list[1:]
print(str_list)
