import os
import sys
import copy
import numpy as np
from scipy import ndimage

def play_round(list_cup, value_destination_max, dict_after):
    list_pick_up = []
    for _ in range(3):
        list_pick_up.append(list_cup.pop(1))

    value_destination = list_cup[0] - 1
    if value_destination < 1:
        value_destination = value_destination_max

    while value_destination in list_pick_up:
        value_destination = value_destination - 1
        if value_destination < 1:
            value_destination = value_destination_max
    

    index_destination = list_cup.index(value_destination)
    for i in range(3):
        list_cup.insert(index_destination + 1  + i, list_pick_up[i])
    
    list_cup.append(list_cup.pop(0))
    return list_cup

def play_round_fast(list_cup, value_destination_max, dict_after):
    val_head = list_cup.pop(0)
    str_head = str(val_head)
    if str_head in dict_after:
        list_insert = dict_after[str_head]
        del dict_after[str_head]
        list_cup = list_insert + list_cup
        
        
    list_pick_up = []
    for i in range(3):
        value_pickup = list_cup.pop(0)
        list_pick_up.append(value_pickup)
        if str(value_pickup) in dict_after:
            list_insert = dict_after[str(value_pickup)]
            del dict_after[str(value_pickup)]
            if i == 0:
                list_pick_up.extend(list_insert[:2])
                list_cup = list_insert[2:] + list_cup
                break
            elif i == 1:
                list_pick_up.extend(list_insert[:1])
                list_cup = list_insert[1:] + list_cup
                break
            else: 
                list_cup = list_insert[0:] + list_cup
                break
            
        

    value_destination = val_head - 1
    if value_destination < 1:
        value_destination = value_destination_max

    while value_destination in list_pick_up:
        value_destination = value_destination - 1
        if value_destination < 1:
            value_destination = value_destination_max
    
    dict_after[str(value_destination)] = list_pick_up
    
    list_cup.append(val_head)
    return list_cup


def play_round_faster(list_cup, value_destination_max, list_after):
    val_head = list_cup.pop(0)
    if list_after[val_head]:
        list_insert = list_after[val_head]
        list_after[val_head] = None
        list_cup = list_insert + list_cup
        
        
    list_pick_up = []
    for i in range(3):
        value_pickup = list_cup.pop(0)
        list_pick_up.append(value_pickup)
        if list_after[value_pickup]:
            list_insert = list_after[value_pickup]
            list_after[value_pickup] = None
            if i == 0:
                list_pick_up.extend(list_insert[:2])
                list_cup = list_insert[2:] + list_cup
                break
            elif i == 1:
                list_pick_up.extend(list_insert[:1])
                list_cup = list_insert[1:] + list_cup
                break
            else: 
                list_cup = list_insert[0:] + list_cup
                break

    value_destination = val_head - 1
    if value_destination < 1:
        value_destination = value_destination_max

    while value_destination in list_pick_up:
        value_destination = value_destination - 1
        if value_destination < 1:
            value_destination = value_destination_max
    
    list_after[value_destination] = list_pick_up
    
    list_cup.append(val_head)
    return list_cup

def play_round_fastest(list_next, index_current):
    # print('list')
    # print(linearize_fastest(list_next, index_current))
    
    pick_up_0 = list_next[index_current]
    pick_up_1 = list_next[pick_up_0]
    pick_up_2 = list_next[pick_up_1]
        
    list_next[index_current] = list_next[pick_up_2]
    list_pick_up = [pick_up_0, pick_up_1, pick_up_2]
    # print('list_pick_up')
    # print([pick_up + 1 for pick_up in list_pick_up])

    value_destination = index_current - 1
    # print('value_destination')
    # print(value_destination)
    if value_destination < 0:
        value_destination = value_destination_max

    while value_destination in list_pick_up:
        value_destination = value_destination - 1
        if value_destination < 0:
            value_destination = value_destination_max

    # print('dest')
    # print(value_destination + 1)
    
    temp = list_next[value_destination]
    list_next[value_destination] = pick_up_0
    list_next[pick_up_2] = temp

    return list_next[index_current]




def linearize_fast(list_cup, dict_after):
    i = 0
    while i < len(list_cup):
        
        if str(list_cup[i]) in dict_after:

            list_insert = dict_after[str(list_cup[i])]
            list_cup.insert(i + 1, list_insert[2])
            list_cup.insert(i + 1, list_insert[1]) 
            list_cup.insert(i + 1, list_insert[0])
            del dict_after[str(list_cup[i])]
        else:
            i += 1
    return list_cup

def linearize_faster(list_cup, list_after):
    i = 0
    while i < len(list_cup):
        
        if list_after[list_cup[i]]:
            list_insert = list_after[list_cup[i]]
            list_after[list_cup[i]] = None
            list_cup.insert(i + 1, list_insert[2])
            list_cup.insert(i + 1, list_insert[1]) 
            list_cup.insert(i + 1, list_insert[0])
        else:
            i += 1
    return list_cup

def delinearalize_fastest(list_cup):
    list_next = [0] * len(list_cup)
    for i in range(len(list_cup) - 1):
        list_next[list_cup[i] - 1] = list_cup[i + 1] - 1
    list_next[list_cup[-1] - 1] = list_cup[0] - 1
    return list_next, list_cup[0] - 1
    

def linearize_fastest(list_next, index_current):
    list_cup = [index_current + 1]
    index_first = index_current
    index_current = list_next[index_current]
    while index_current != index_first:
        list_cup.append(index_current + 1)
        index_current = list_next[index_current]
    return list_cup

# part 1 A
list_cup = [3,6,2,9,8,1,7,5,4]
value_destination_max = len(list_cup)
dict_after = {}
for i in range(10):
    list_cup = play_round(list_cup, value_destination_max, dict_after)
   
index_1 = list_cup.index(1)
list_cup = list_cup [index_1:] + list_cup [:index_1]
print(list_cup[1:])

# part 1 B
list_cup = [3,6,2,9,8,1,7,5,4]
value_destination_max = len(list_cup)
dict_after = {}
for i in range(10):
    list_cup = play_round_fast(list_cup, value_destination_max, dict_after)

list_cup = linearize_fast(list_cup, dict_after)
index_1 = list_cup.index(1)
list_cup = list_cup [index_1:] + list_cup [:index_1]
print(list_cup[1:])


# part 1 C
list_cup = [3,6,2,9,8,1,7,5,4]
value_destination_max = len(list_cup)
list_after = [None] * (len(list_cup)  + 1)
for i in range(10):
    list_cup = play_round_faster(list_cup, value_destination_max, list_after)

list_cup = linearize_faster(list_cup, list_after)
index_1 = list_cup.index(1)
list_cup = list_cup [index_1:] + list_cup [:index_1]
print(list_cup[1:])


# part 1 D

list_cup = [3,6,2,9,8,1,7,5,4]
# list_cup = [3,8,9,1,2,5,4,6,7]
list_next, index_current = delinearalize_fastest(list_cup)
value_destination_max = len(list_cup) - 1
index_current = list_cup[0] - 1
for i in range(10):
    index_current = play_round_fastest(list_next, index_current)

list_cup = linearize_fastest(list_next, index_current)
index_1 = list_cup.index(1)
list_cup = list_cup [index_1:] + list_cup [:index_1]
print(list_cup[1:])


# part 2
list_cup = [3,6,2,9,8,1,7,5,4]
# list_cup = [3,8,9,1,2,5,4,6,7]
for i in range(10, 1000001):
    list_cup.append(i)
list_next, index_current = delinearalize_fastest(list_cup)
value_destination_max = len(list_cup) - 1
index_current = list_cup[0] - 1
for i in range(10000000):
    if (i % 10000) == 0:
        print(i)
        sys.stdout.flush()
    index_current = play_round_fastest(list_next, index_current)

list_cup = linearize_fastest(list_next, index_current)
index_1 = list_cup.index(1)
list_cup = list_cup [index_1:] + list_cup [:index_1]
print(list_cup[1] * list_cup[2])

# print(list_cup)