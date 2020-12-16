import os
import sys
import numpy as np
import math

with open('input.txt', 'r') as file:
    list_line = file.readlines()
list_line = [line.strip() for line in list_line]


#parse
list_field = []
list_ticket = []
list_list_ticket_near = []
index_line = 0
# parse field
while index_line < len(list_line):
    line = list_line[index_line]
    if line == '':
        index_line += 1
        index_line += 1
        break
    else:
        field = {}
        field['name_field'] = line.split(':')[0]
        field['min_a'] = int(line.split(':')[1][1:].split(' or ')[0].split('-')[0])
        field['max_a'] = int(line.split(':')[1][1:].split(' or ')[0].split('-')[1])
        field['min_b'] = int(line.split(':')[1][1:].split(' or ')[1].split('-')[0])
        field['max_b'] = int(line.split(':')[1][1:].split(' or ')[1].split('-')[1])
        list_field.append(field)
        index_line += 1

# parse ticket
while index_line < len(list_line):
    line = list_line[index_line]
    if line == '':
        index_line += 1
        index_line += 1
        break
    else:
        line = list_line[index_line]
        list_ticket = [int(str_ticket) for str_ticket in line.split(',')]
        index_line += 1
# parse near
while index_line < len(list_line):
    line = list_line[index_line]
    list_list_ticket_near.append([int(str_ticket) for str_ticket in line.split(',')])
    index_line += 1



def is_within_field(field, ticket):
    if field['min_a'] <= ticket and ticket <= field['max_a']:
        return True
    if field['min_b'] <= ticket and ticket <= field['max_b']:
        return True
    return False

# part 1
list_list_ticket_valid = []
sum_invalid = 0
for list_ticket_near in list_list_ticket_near:
    is_valid_ticked = True
    for ticket in list_ticket_near:
        fits_field = False
        for field in list_field:
            if is_within_field(field, ticket):
                fits_field = True
                break
        if not fits_field:
            sum_invalid += ticket
            is_valid_ticked = False
    if is_valid_ticked:
        list_list_ticket_valid.append(list_ticket_near)
print(sum_invalid)

# part 2
dict_index_ticket_to_field = {}
dict_field_to_index_ticket = {}
for round_val in range(20):
    for index_field, field in enumerate(list_field):
        if field['name_field'] in dict_field_to_index_ticket:
            continue
        list_index_possible = []
        for index_ticket in range(len(list_field)):
            if str(index_ticket) in dict_index_ticket_to_field:
                continue
            is_posibile_index = True
            for list_ticket_near in list_list_ticket_valid:
                if not is_within_field(field, list_ticket_near[index_ticket]):
                    is_posibile_index = False
                    break
            if is_posibile_index:
                
                list_index_possible.append(index_ticket)
        if len(list_index_possible) == 1:
            dict_field_to_index_ticket[field['name_field']] = list_index_possible[0]
            dict_index_ticket_to_field[str(list_index_possible[0])] = field['name_field']
            print(field['name_field'] + ': ' + str(list_index_possible[0]) )
        
list_dep = []
list_dep.append('departure location')
list_dep.append('departure station')
list_dep.append('departure platform')
list_dep.append('departure track')
list_dep.append('departure date')
list_dep.append('departure time')

mult = 1
for dep in list_dep:
    mult *= list_ticket[dict_field_to_index_ticket[dep]]
print(mult)
    