import os
import sys
import numpy as np
from scipy import ndimage

with open('input.txt', 'r') as file:
    list_line = file.readlines()
list_line = [line.strip() for line in list_line]

def array_to_id_border(array):
    id_border = ''
    list_array = array.tolist()
    for i in range(len(array)):
        id_border += str(list_array[i])
    return id_border

def get_id_border(tile, index_border, index_flip):
    if index_flip == 0:
        if index_border == 0:
            return array_to_id_border(tile['array'][0,:])
        elif index_border == 1:
            return array_to_id_border(tile['array'][:,9])
        elif index_border == 2:
            return array_to_id_border(np.flip(tile['array'][9,:]))
        elif index_border == 3:
            return array_to_id_border(np.flip(tile['array'][:,0]))
    else:
        if index_border == 0:
            return array_to_id_border(np.flip(tile['array'][0,:]))
        elif index_border == 1:
            return array_to_id_border(tile['array'][:,0])
        elif index_border == 2:
            return array_to_id_border(tile['array'][9,0:])
        elif index_border == 3:
            return array_to_id_border(np.flip(tile['array'][:,9]))


#parse
list_tile = []
tile = {}
tile['id_tile'] = ''
tile['array'] = np.zeros((10,10), dtype=int)
index_line = 0
for line in list_line:
    if line == '':
        list_tile.append(tile)
        tile = {}
        tile['id_tile'] = ''
        tile['array'] = np.zeros((10,10), dtype=int)
        index_line = 0
    elif 'Tile' in line:
        tile['id_tile'] = line[5:-1]
    else:
        for index_char, char in enumerate(line):
            if char == '#':
                tile['array'][index_line, index_char] = 1
        index_line += 1

list_tile.append(tile)
#indexing
dict_tile = {}
for tile in list_tile:
    dict_tile[tile['id_tile']] = tile

dict_border = {}
for tile in list_tile:
    for index_border in range(4):
        for index_orientation in range(2):
            id_border = get_id_border(tile, index_border, index_orientation)
            if id_border not in dict_border:
                dict_border[id_border] = []
            dict_border[id_border].append(tile['id_tile'])

def find_list_corner(list_tile, dict_border):
    list_corner = []
    for tile in list_tile:
        list_singlar = []
        for index_border in range(4):
            id_border = get_id_border(tile, index_border, index_orientation)
            if 1 == len(dict_border[id_border]):
                list_singlar.append(index_orientation)
        if len(list_singlar) == 2:
            list_corner.append(tile['id_tile'])
    return list_corner
    

def place_tile(dict_tile, dict_tile_used, array_full, array_id_tile, id_tile, x, y, id_border_match):
    tile = dict_tile[id_tile]
    array_id_tile[y, x] = int(id_tile)
    dict_tile_used[id_tile] = True
    # fit array
    array = tile['array']
    for _ in range(4):

        y_start = (10*y)
        y_end = y_start + 10
        x_start = (10*x)
        x_end = x_start + 10


        array_full[y_start:y_end, x_start:x_end] = array
     
        if x == 0:
            id_border = array_to_id_border(array_full[(y*10), 0:10])
        else:
            id_border = array_to_id_border(array_full[y*10:(y+1)*10, (x*10)])

        if id_border == id_border_match:
            return

        array = np.rot90(array)

    array = np.flip(array, axis=1)
    for _ in range(4):


        y_start = (10*y)
        y_end = y_start + 10
        x_start = (10*x)
        x_end = x_start + 10
        array_full[y_start:y_end, x_start:x_end] = array

        if x == 0:
            id_border = array_to_id_border(array_full[(y*10), 0:10])
        else:
            id_border = array_to_id_border(array_full[y*10:(y+1)*10, (x*10)])
        
        if id_border == id_border_match:
            return
        array = np.rot90(array)
    raise Exception('not found')

# part 1
list_corner = find_list_corner(list_tile, dict_border)
prod = 1
for corner in list_corner:
    prod *= int(corner)
print(prod)

# build puzzle
dict_tile_used = {}
array_full = np.zeros((120, 120), dtype=int)
array_tile = np.zeros((12, 12), dtype=int)

# place corner
id_corner_top_left = list_corner[0]
tile = dict_tile[id_corner_top_left]
rota = 0
if 1 == len(dict_border[get_id_border(tile, 1, 0)]):
    rota = 1
    if 1 == len(dict_border[get_id_border(tile, 2, 0)]):
        rota = 2
else:
    if 1 == len(dict_border[get_id_border(tile, 2, 0)]):
        rota = 3

array = tile['array']      
for _ in range(rota):
    array = np.rot90(array)

array_full[0:10, 0:10] = array
array_tile[0,0] = int(id_corner_top_left)
dict_tile_used[id_corner_top_left] = True

for y in range(0, 12):
    for x in range(0, 12):
        if (x == 0) and (y == 0):
            continue
        if x == 0:
            id_border = array_to_id_border(array_full[y*10 - 1, 0:10])
        else:
            id_border = array_to_id_border(array_full[y*10:(y+1)*10, x*10 - 1])
        list_id_tile = dict_border[id_border]
        if list_id_tile[0] in dict_tile_used:
            id_tile = list_id_tile[1]
        else:
            id_tile = list_id_tile[0]
            
        place_tile(dict_tile, dict_tile_used, array_full, array_tile, id_tile, x, y, id_border)
        
# part 2
list_line_seamonster = []
list_line_seamonster.append('                  # ')
list_line_seamonster.append('#    ##    ##    ###')
list_line_seamonster.append(' #  #  #  #  #  #   ')

array_seamonser = np.zeros((3, len(list_line_seamonster[0])), dtype=int)
for index_line, line in enumerate(list_line_seamonster):
    for index_char, char in enumerate(line):
        if char == '#':
            array_seamonser[index_line, index_char] = 1
size_monster = np.count_nonzero(array_seamonser)



array_cut = np.zeros((12*8, 12*8), dtype=int)
for y in range(0, 12):
    for x in range(0, 12):
        tile = array_full[10*y:10*(y+1), 10*x:10*(x+1)]
        tile_cut = tile[1:9, 1:9]
        array_cut[8*y:8*(y+1), 8*x:8*(x+1)] = tile_cut


array_full = array_cut

array_full = np.rot90(array_full)
array_full = np.rot90(array_full)
array_full = np.rot90(array_full)
array_score = ndimage.filters.convolve(array_full, np.flip(array_seamonser), mode='constant', cval=0)
array_location = np.zeros(array_full.shape)
array_location[array_score == size_monster] = 1
count_monster = np.count_nonzero(array_location)
count_min = 5
count_rough = np.count_nonzero(array_full) - (size_monster * count_monster)
print(count_rough)
# 3450
# below 3544