import os
import sys
import copy
import numpy as np
from scipy import ndimage

with open('input.txt', 'r') as file:
    list_line = file.readlines()
list_line = [line.strip() for line in list_line]

#parse
list_card_1 = []
index_line = 0
while index_line < len(list_line):
    line = list_line[index_line]
    index_line += 1
    if line == '':
        break
    if 'Player' in line:
        continue
    list_card_1.append(int(line))

list_card_2 = []
while index_line < len(list_line):
    line = list_line[index_line]
    index_line += 1
    if line == '':
        break
    if 'Player' in line:
        continue
    list_card_2.append(int(line))

list_card_1_copy = copy.copy(list_card_1)
list_card_2_copy = copy.copy(list_card_2)

#part_1
while (0 < len(list_card_1)) and (0 < len(list_card_2)):
    card_1 = list_card_1.pop(0)
    card_2 = list_card_2.pop(0)
    if card_1 < card_2:
        list_card_2.append(card_2)
        list_card_2.append(card_1)
    else:
        list_card_1.append(card_1)
        list_card_1.append(card_2)

if 0 < len(list_card_1):
    list_card_win = list_card_1
else:
    list_card_win = list_card_2
    
score = 0
for index_card, card in enumerate(list_card_win):
    score += (len(list_card_win) - index_card) * card
print(score)




#part_2
def create_hash(list_card_1, list_card_2):
    return str(list_card_1) + str(list_card_2)

def play_game(list_card_1, list_card_2):
    count_round = 1
    dict_hash_state = {}
    while (0 < len(list_card_1)) and (0 < len(list_card_2)):
        count_round += 1
        hash_state = create_hash(list_card_1, list_card_2)
        # rule 1: hashing
        if hash_state in dict_hash_state:
            return True, list_card_1, list_card_2
        else:
            dict_hash_state[hash_state] = True

        card_1 = list_card_1.pop(0)
        card_2 = list_card_2.pop(0)
        if (card_1 <= len(list_card_1)) and (card_2 <= len(list_card_2)):
            # rule 2: recusion game
            is_won_by_1, _, _ = play_game(list_card_1[:card_1], list_card_2[:card_2])
        else:
            # rule 3: higher value
            is_won_by_1 = card_2 < card_1

        if is_won_by_1:
            list_card_1.append(card_1)
            list_card_1.append(card_2)
        else:
            list_card_2.append(card_2)
            list_card_2.append(card_1)

    if 0 < len(list_card_1):
        return True, list_card_1, list_card_2
    else:
        return False, list_card_1, list_card_2

    

        

list_card_1 = list_card_1_copy
list_card_2 = list_card_2_copy


is_won_by_one, list_card_1, list_card_2 = play_game(list_card_1, list_card_2)

# compute score
if is_won_by_one:
    list_card_win = list_card_1
else:
    list_card_win = list_card_2
    
score = 0
for index_card, card in enumerate(list_card_win):
    score += (len(list_card_win) - index_card) * card
print(score)