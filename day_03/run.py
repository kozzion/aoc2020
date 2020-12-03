import os
import sys
import json

with open('input.txt', 'r') as file:
    list_line = file.readlines()
list_line = [line.strip() for line in list_line]
len_line = len(list_line[0])

def compute_for_slope(list_line, len_line, slope):
    index_y = 0
    index_x = 0
    count = 0
    while index_y < len(list_line):
        if list_line[index_y][index_x] == '#':
            count += 1
        index_y = (index_y + slope[0])
        index_x = (index_x + slope[1]) % len_line
    return count

# part 1
slope = (1, 3)
print(compute_for_slope(list_line, len_line, slope))

# part 2
list_slope = []
list_slope.append((1,1))
list_slope.append((1,3))
list_slope.append((1,5))
list_slope.append((1,7))
list_slope.append((2,1))

product = 1
for slope in list_slope:
    product *= compute_for_slope(list_line, len_line, slope)
 
print(product)