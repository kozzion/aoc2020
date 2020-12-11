import os
import sys
import numpy as np
from scipy import signal

with open('input.txt', 'r') as file:
    list_line = file.readlines()
list_line = [line.strip() for line in list_line]

#parse
size_0 = len(list_line)
size_1 = len(list_line[0])

array_mask_seat = np.zeros((size_0, size_1), dtype=np.bool)
for index_0, line in enumerate(list_line):
    for index_1, char in enumerate(line):
        if char == 'L':
            array_mask_seat[index_0, index_1] = True

def advance_1(array_mask_occupied, array_mask_seat):
    array_neighbours = np.zeros(array_mask_occupied.shape, dtype=np.int32)
    array_mask_occupied_new = np.zeros(array_mask_occupied.shape, dtype=np.bool)
    array_neighbours[array_mask_occupied] = 1
    array_neighbourhood = np.ones((3, 3), dtype=np.int32)

    # array_neighbours = signal.convolve2d(array_neighbours, array_neighbourhood, boundary='symm', mode='same')
    array_neighbours = signal.convolve2d(array_neighbours, array_neighbourhood, mode='same')
    array_mask_occupied_new[(array_neighbours == 0) & (array_mask_seat == True)] = True
    array_mask_occupied_new[(array_neighbours < 5) & (array_mask_occupied == True)] = True
    array_mask_occupied_new[(5 <= array_neighbours) & (array_mask_occupied == True)] = False
    return array_mask_occupied_new


def is_occupied_visible_direction(array_mask_occupied, array_mask_seat, point, direction):
    point = point + direction
    while (0 <= point[0]) & (point[0] < array_mask_occupied.shape[0]) & (0 <= point[1]) & (point[1] < array_mask_occupied.shape[1]):
        if array_mask_seat[point[0], point[1]]:
            if array_mask_occupied[point[0], point[1]]:
                return 1
            else:
                return 0
        point = point + direction
    return 0

def count_occupied_visible(array_mask_occupied, array_mask_seat, point):
    count_occupied_visible = 0
    count_occupied_visible += is_occupied_visible_direction(array_mask_occupied, array_mask_seat, point, np.array([ 0, 1]))
    count_occupied_visible += is_occupied_visible_direction(array_mask_occupied, array_mask_seat, point, np.array([ 1, 0]))
    count_occupied_visible += is_occupied_visible_direction(array_mask_occupied, array_mask_seat, point, np.array([ 0,-1]))
    count_occupied_visible += is_occupied_visible_direction(array_mask_occupied, array_mask_seat, point, np.array([-1, 0]))
    count_occupied_visible += is_occupied_visible_direction(array_mask_occupied, array_mask_seat, point, np.array([ 1, 1]))
    count_occupied_visible += is_occupied_visible_direction(array_mask_occupied, array_mask_seat, point, np.array([-1, 1]))
    count_occupied_visible += is_occupied_visible_direction(array_mask_occupied, array_mask_seat, point, np.array([-1,-1]))
    count_occupied_visible += is_occupied_visible_direction(array_mask_occupied, array_mask_seat, point, np.array([ 1,-1]))
    return count_occupied_visible

def advance_2(array_mask_occupied, array_mask_seat):
    array_mask_occupied_new = np.zeros(array_mask_occupied.shape, dtype=np.bool)
    for i in range(array_mask_seat.shape[0]):
        for j in range(array_mask_seat.shape[1]):
            if array_mask_seat[i,j]:
                occupied_visible = count_occupied_visible(array_mask_occupied, array_mask_seat, np.array([i,j]))
                if array_mask_occupied[i,j] == False:
                    if occupied_visible == 0: 
                        array_mask_occupied_new[i,j] = True
                else:
                    if occupied_visible < 5: 
                        array_mask_occupied_new[i,j] = True
                    else:
                        array_mask_occupied_new[i,j] = False
    return array_mask_occupied_new
    
#part 1
array_mask_occupied = np.zeros((size_0, size_1), dtype=np.bool)
array_mask_occupied_new = advance_1(array_mask_occupied, array_mask_seat)

while not np.array_equal(array_mask_occupied_new, array_mask_occupied):
    array_mask_occupied = array_mask_occupied_new
    array_mask_occupied_new = advance_1(array_mask_occupied, array_mask_seat)

print(np.count_nonzero(array_mask_occupied))

#part 2
array_mask_occupied = np.zeros((size_0, size_1), dtype=np.bool)
array_mask_occupied_new = advance_2(array_mask_occupied, array_mask_seat)
while not np.array_equal(array_mask_occupied_new, array_mask_occupied):
    array_mask_occupied = array_mask_occupied_new
    array_mask_occupied_new = advance_2(array_mask_occupied, array_mask_seat)

print(np.count_nonzero(array_mask_occupied))