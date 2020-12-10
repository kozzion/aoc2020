import os
import sys
import json
import copy

with open('input.txt', 'r') as file:
    list_line = file.readlines()
list_line = [line.strip() for line in list_line]

#parse
list_number = [int(line) for line in list_line]
list_number_sorted = sorted(list_number)
     
#part 1
count_jolt_1 = 0
count_jolt_3 = 0
jolt = 0
for number in list_number_sorted:
    if number - jolt == 1:
        count_jolt_1 += 1
    else:
        count_jolt_3 += 1
    jolt = number
count_jolt_3 += 1
print(count_jolt_1 * count_jolt_3)

#part 2
jolt = 0
list_size_garden = []
size_garden = 1
for number in list_number_sorted:
    diff = number - jolt
    if number - jolt == 1:
        size_garden += 1
    else:
        list_size_garden.append(size_garden)
        size_garden = 1
    jolt = number
list_size_garden.append(size_garden)


list_garden_perm = [1, 1, 1, 2, 4, 7]
count_perm = 1
for size_garden in list_size_garden:
    count_perm *= list_garden_perm[size_garden]
print(count_perm)
