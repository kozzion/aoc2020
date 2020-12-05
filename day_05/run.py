import os
import sys
import json

with open('input.txt', 'r') as file:
    list_line = file.readlines()
list_line = [line.strip() for line in list_line]



def str_seat_to_id_seat(str_seat:str):
    str_seat = str_seat.replace('F', '0')
    str_seat = str_seat.replace('B', '1')
    str_seat = str_seat.replace('R', '1')
    str_seat = str_seat.replace('L', '0')
    return int(str_seat, 2), int(str_seat[:7], 2), int(str_seat[7:], 2) 

list_id_seat = [str_seat_to_id_seat(line)[0] for line in list_line]
list_index_row = [str_seat_to_id_seat(line)[1] for line in list_line]
list_index_col = [str_seat_to_id_seat(line)[2] for line in list_line]

# part 1
print(max(list_id_seat))

# part 2 
# Okay nu had ik teveel plezier
list_list_id_seat = []
list_list_seat = []

for i in range(127):
    list_list_id_seat.append([None] * 8)
    list_list_seat.append('O' * 8)
    
for id_seat, index_row, index_col in zip(list_id_seat, list_index_row, list_index_col):
    list_list_id_seat[index_row][index_col] = id_seat
    list_list_seat[index_row] = list_list_seat[index_row][:index_col] + 'X' + list_list_seat[index_row][index_col + 1:]

for index, list_seat in enumerate(list_list_seat):
    print(str(index * 8).ljust(4) + ' ' + str(list_seat))