import os
import sys
import numpy as np
import math



def add_number(list_number):
    last_number = list_number[-1]
    for i in range(1, len(list_number)):
        if list_number[-(i + 1)] == last_number:
            list_number.append(i)
            return
    list_number.append(0)

def add_number_fast(list_number, dict_number):
    last_number = list_number[-1]
    str_last_number = str(last_number)
    if not str_last_number in dict_number:
        new_number = 0    
    else:
        time_since_spoken = len(list_number) - dict_number[str_last_number]
        new_number = time_since_spoken
    
    list_number.append(new_number)
    dict_number[str(list_number[-2])] = len(list_number) - 1

# part 1
list_number = [12,1,16,3,11,0]
for i in range(2017):
    add_number(list_number)
print(list_number[2019])

# part 2
list_number = [12,1,16,3,11,0]

dict_number = {}
for i in range(len(list_number) - 1):
    dict_number[str(list_number[i])] = i + 1

for i in range(30000000):
    if i % 10000 == 0:
        print(i)
        sys.stdout.flush()
    add_number_fast(list_number, dict_number)

print(list_number[30000000 - 1])
