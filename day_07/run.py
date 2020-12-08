import os
import sys
import json

with open('input.txt', 'r') as file:
    list_line = file.readlines()
list_line = [line.strip() for line in list_line]

# parse
dict_bag = {}
for line in list_line:
    str_container = line.split(' contain ')[0]
    
    id_container = str_container.split(' ')[0] + ' ' + str_container.split(' ')[1]
    dict_bag[id_container] = []
    
    if line.split(' contain ')[1] == 'no other bags.':
        continue
    else:
        list_contain = line.split(' contain ')[1].split(',') 
        for contain in list_contain:
            contain = contain.strip()
            count = int(contain.split(' ')[0])
            id_contain = (contain.split(' ')[1] + ' ' + contain.split(' ')[2]).strip()
            dict_bag[id_container].append((count, id_contain))


def can_contain_shiny_gold(dict_bag, id_bag):
    for count, id_bag_inner in dict_bag[id_bag]:
        if id_bag_inner == 'shiny gold':
            return True
        else:
            if can_contain_shiny_gold(dict_bag, id_bag_inner):
                return True
    return False

def count_inside(dict_bag, id_bag):
    count = 0
    for count_inner, id_bag_inner in dict_bag[id_bag]:
        count += count_inner
        count += count_inner * count_inside(dict_bag, id_bag_inner)
    return count

#part 1
count = 0
for id_bag in dict_bag:
    if can_contain_shiny_gold(dict_bag, id_bag):
        count += 1
print(count)

#part 2
print(count_inside(dict_bag, 'shiny gold'))
