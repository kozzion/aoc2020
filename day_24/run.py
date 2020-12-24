import os
import sys
import copy
import numpy as np
from scipy import ndimage

with open('input.txt', 'r') as file:
    list_line = file.readlines()
list_line = [line.strip() for line in list_line]

#parse
list_list_move = []
for line in list_line:
    list_move = []
    while 0 < len(line):
        move = line[0]
        line = line[1:]
        if move in ['s', 'n']:
            move += line[0]
            line = line[1:]
        list_move.append(move)
    list_list_move.append(list_move)
    

def list_move_to_coord(x, y, list_move):
    for move in list_move:
        if move == 'e':
            x +=1
        if move == 'w':
            x -=1
        if y % 2 == 0:
            if move == 'ne':
                y += 1
            if move == 'nw':
                y += 1
                x -=1
            if move == 'se':
                y -= 1
            if move == 'sw':
                y -= 1
                x -=1
        else:
            if move == 'ne':
                y += 1
                x +=1
            if move == 'nw':
                y += 1
            if move == 'se':
                y -= 1
                x +=1
            if move == 'sw':
                y -= 1
                
    return x, y 

def advance(dict_black):
    dict_count = {}
    for key in dict_black:
        dict_count[key] = 0

    list_list_move = [['e'], ['w'], ['ne'], ['nw'], ['se'], ['sw']]
    for (x, y) in dict_black.values():
        for list_move in list_list_move:
            x_end, y_end = list_move_to_coord(x, y, list_move)
            key = str([x_end, y_end])
            if not key in dict_count:
                dict_count[key] = 0
            dict_count[key] += 1

    # print(dict_count)
    dict_black_new = {}
    for key, count in dict_count.items():
        if key in dict_black:
            if (count == 1) or (count == 2):
                dict_black_new[key] = (int(key[1:-1].split(', ')[0]), int(key[1:-1].split(', ')[1]))
        else:
            if count == 2:
                dict_black_new[key] = (int(key[1:-1].split(', ')[0]), int(key[1:-1].split(', ')[1]))
    return dict_black_new
#part 1
dict_black = {}
for list_move in list_list_move:
    x, y = list_move_to_coord(0, 0, list_move)
    key = str([x, y])
    if key in dict_black:
        del dict_black[key]
    else:
        dict_black[key] = (x, y)
print(len(dict_black))

#part 2
for i in range(100):
    dict_black = advance(dict_black)
print(len(dict_black))