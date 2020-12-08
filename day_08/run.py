import os
import sys
import json
import copy

with open('input.txt', 'r') as file:
    list_line = file.readlines()
list_line = [line.strip() for line in list_line]

# parse
def run_line(list_line, index_line, acc):
    line =list_line[index_line]
    com = line[:3]
    opp = line[4]
    val = int(line[5:])
    if com == 'nop':
        return index_line + 1, acc
    elif com == 'acc':
        if opp == '+':
            return index_line + 1, acc + val
        if opp == '-':
            return index_line + 1, acc - val

    elif com == 'jmp':
        if opp == '+':
            return index_line + val, acc
        if opp == '-':
            return index_line - val, acc

def run_program(list_line):
    dict_line = {}
    index_line = 0
    acc = 0
    while not str(index_line) in dict_line:
        dict_line[str(index_line)] = True
        index_line, acc = run_line(list_line, index_line, acc)
        if index_line == len(list_line):
            return True, index_line, acc
    return False, index_line, acc
    
#part 1
print(run_program(list_line)[2])

#part 2
for index, line in enumerate(list_line):
    com = line[:3]
    if com == 'acc':
        continue
    elif com == 'jmp':
        line_mod = 'nop' + line[3:]
    elif com == 'nop':
        line_mod = 'jmp' + line[3:]

    list_line_mod = copy.deepcopy(list_line)
    list_line_mod[index] = line_mod
    
    is_succes, index_line, acc = run_program(list_line_mod)
    if is_succes:
        print(acc)
        break
