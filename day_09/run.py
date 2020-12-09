import os
import sys
import json
import copy

with open('input.txt', 'r') as file:
    list_line = file.readlines()
list_line = [line.strip() for line in list_line]

#parse
list_number = [int(line) for line in list_line]


def build_dict_sum(list_number_component):
    dict_sum = {}
    for i in range(len(list_number_component)):
        for j in range(i + 1, len(list_number_component)):
            str_sum = str(list_number_component[i] + list_number_component[j])
            dict_sum[str_sum] = True
    return dict_sum

def check_number(list_number_component, number_sum):
    dict_sum = build_dict_sum(list_number_component)
    return str(number_sum) in dict_sum
     
#part 1
for index, number in enumerate(list_number):
    if index < 25:
        continue
    else:
        is_valid = check_number(list_number[index - 25: index], list_number[index])
        if not is_valid:
            print(number)
            break

#part 2
number_target = 3199139634
index_lower = 0
index_upper = 0
number_sum = list_number[0]
while number_sum != number_target:
    if number_sum < number_target:
        index_upper += 1
        number_sum += list_number[index_upper]
    else:
        number_sum -= list_number[index_lower]
        index_lower += 1

number_min = min(list_number[index_lower:index_upper+ 1] )
number_max = max(list_number[index_lower:index_upper+ 1] )
print(number_min + number_max)