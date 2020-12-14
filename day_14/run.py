import os
import sys
import numpy as np
import math

with open('input.txt', 'r') as file:
    list_line = file.readlines()
list_line = [line.strip() for line in list_line]

#parse
def int_value_to_str_value(int_value):
    lenght = 36
    list_str_digit = [str(digit) for digit in bin(int_value)[2:]]
    str_value = '0' * (lenght - len(list_str_digit))
    for str_digit in list_str_digit:
        str_value += str_digit
    
    return str_value

def apply_mask_1(str_mask, int_value):
    str_value = int_value_to_str_value(int_value)
    for i in range(len(str_value)):
        if str_mask[i] == '1':
            str_value = str_value[:i] + '1' + str_value[i+1:]
        elif str_mask[i] == '0':
            str_value = str_value[:i] + '0' + str_value[i+1:]
    return int(str_value, 2)


def apply_mask_2(str_mask, int_value):
    str_value = int_value_to_str_value(int_value)
    for i in range(36):
        if str_mask[i] == '1':
            str_value = str_value[:i] + '1' + str_value[i+1:]
    list_str_value = [str_value]
    for i_mask in range(36):
        if str_mask[i_mask] == 'X':
            for i_val in range(len(list_str_value)):
                if list_str_value[i_val][i_mask] == '0':
                    list_str_value.append(list_str_value[i_val][:i_mask] + '1' + list_str_value[i_val][i_mask + 1:])
                else:
                    list_str_value.append(list_str_value[i_val][:i_mask] + '0' + list_str_value[i_val][i_mask + 1:])
    return list_str_value

def execute_line_1(dict_mem, str_mask, line):
    if line[0:3] == 'mas':
        str_mask = line.split(' = ')[1]
    else:
        str_address = line.split(' = ')[0][4:-1]
        int_value = int(line.split(' = ')[1])
        int_value = apply_mask_1(str_mask, int_value)
        dict_mem[str_address] = int_value
    return dict_mem, str_mask


def execute_line_2(dict_mem, str_mask, line):
    if line[0:3] == 'mas':
        str_mask = line.split(' = ')[1]
    else:
        int_address = int(line.split(' = ')[0][4:-1])
        int_value = int(line.split(' = ')[1])
        list_str_address = apply_mask_2(str_mask, int_address)
        for str_address in list_str_address:
            dict_mem[str_address] = int_value
    return dict_mem, str_mask


# part 1
dict_mem = {}
str_mask = 'x' * 36
for line in list_line:
    dict_men, str_mask = execute_line_1(dict_mem, str_mask, line)
print(sum(dict_mem.values()))

# part 2
dict_mem = {}
str_mask = 'x' * 36
for line in list_line:
    dict_men, str_mask = execute_line_2(dict_mem, str_mask, line)
print(sum(dict_mem.values()))
