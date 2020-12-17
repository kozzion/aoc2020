import os
import sys
import numpy as np
from scipy import ndimage

with open('input.txt', 'r') as file:
    list_line = file.readlines()
list_line = [line.strip() for line in list_line]


#parse
size_0 = len(list_line)
size_1 = len(list_line[0])
array_active_1 = np.zeros((size_0, size_1, 1), dtype=np.int)
for index_0, line in enumerate(list_line):
    for index_1, char in enumerate(line):
        if char == '#':
            array_active_1[index_0, index_1, 0] = 1

#parse
size_0 = len(list_line)
size_1 = len(list_line[0])
array_active_2 = np.zeros((size_0, size_1, 1, 1), dtype=np.int)
for index_0, line in enumerate(list_line):
    for index_1, char in enumerate(line):
        if char == '#':
            array_active_2[index_0, index_1, 0, 0] = 1
# parse field

def advance_1(array_active):
    array_kernel = np.ones((3,3,3), dtype=np.int)
    array_kernel[1,1,1] = 0
    array_active_padded = np.pad(array_active, ((1,1), (1,1), (1,1)), 'constant')
    array_active_new = np.zeros(array_active_padded.shape, dtype=np.int)
    array_neigbours = ndimage.filters.convolve(array_active_padded, array_kernel, mode='constant', cval=0)
    array_active_new[(array_active_padded == 1) & (array_neigbours == 2)] = 1
    array_active_new[(array_active_padded == 1) & (array_neigbours == 3)] = 1
    array_active_new[(array_active_padded == 0) & (array_neigbours == 3)] = 1
    return array_active_new
    

def advance_2(array_active):
    array_kernel = np.ones((3,3,3,3), dtype=np.int)
    array_kernel[1,1,1,1] = 0
    array_active_padded = np.pad(array_active, ((1,1), (1,1), (1,1), (1,1)), 'constant')
    array_active_new = np.zeros(array_active_padded.shape, dtype=np.int)
    array_neigbours = ndimage.filters.convolve(array_active_padded, array_kernel, mode='constant', cval=0)
    
    array_active_new[(array_active_padded == 1) & (array_neigbours == 2)] = 1
    array_active_new[(array_active_padded == 1) & (array_neigbours == 3)] = 1
    array_active_new[(array_active_padded == 0) & (array_neigbours == 3)] = 1
    return array_active_new

#part 1
for i in range(6):
    array_active_1 = advance_1(array_active_1)
print(np.count_nonzero(array_active_1))

#part 2
for i in range(6):
    array_active_2 = advance_2(array_active_2)
print(np.count_nonzero(array_active_2))