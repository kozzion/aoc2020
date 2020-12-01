import os
import sys
import json

with open('input.txt', 'r') as file:
    list_lines = file.readlines()

list_number = [int(line) for line in list_lines] 
min_val = min(list_number)
# part 1
for i, number_a in enumerate(list_number):
    for j, number_b in enumerate(list_number):
        if i != j and (number_a + number_b == 2020):
            print(number_a * number_b)
            break

# part 2
count = 0
for i, number_a in enumerate(list_number):
    for j, number_b in enumerate(list_number):
        if i != j and ((number_a + number_b) <= (2020 - min_val)): # small speedup
            for h, number_c in enumerate(list_number):
                if i != h and (number_a + number_b + number_c == 2020):
                    print(number_a * number_b * number_c)
                    break
