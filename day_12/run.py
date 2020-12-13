import os
import sys
import copy

with open('input.txt', 'r') as file:
    list_line = file.readlines()
list_line = [line.strip() for line in list_line]

def rotate_right(facing, amount):
    if amount < 0:
        raise Exception()
    count = amount // 90
    for i in range(count):
        if facing == 'N':
            facing = 'E'
        elif facing == 'E':
            facing = 'S'
        elif facing == 'S':
            facing = 'W'
        elif facing == 'W':
            facing = 'N'
    return facing

def advance_1(state, line_instuction):
    instuction = line_instuction[0]
    amount = int(line_instuction[1:])
    state = copy.deepcopy(state)

    if instuction == 'L':
        instuction = 'R'
        amount = 360 - amount

    if instuction == 'F':
        instuction = state['f']
    if instuction == 'E':
        state['x'] += amount
    elif instuction == 'W':
        state['x'] -= amount
    elif instuction == 'N':
        state['y'] += amount
    elif instuction == 'S':
        state['y'] -= amount
    
    elif instuction == 'R':
        state['f'] = rotate_right(state['f'], amount)
    
    return state


def advance_2(state, line_instuction):
    instuction = line_instuction[0]
    amount = int(line_instuction[1:])
    state = copy.deepcopy(state)

    if instuction == 'L':
        instuction = 'R'
        amount = 360 - amount

    if instuction == 'E':
        state['vx'] += amount
    elif instuction == 'W':
        state['vx'] -= amount
    elif instuction == 'N':
        state['vy'] += amount
    elif instuction == 'S':
        state['vy'] -= amount
    
    elif instuction == 'R':
        count = amount // 90
        for _ in range(count):
            vx = state['vx']
            vy = state['vy']
            state['vx'] = vy
            state['vy'] = -vx
    elif instuction == 'F':
        state['x'] += state['vx'] * amount
        state['y'] += state['vy'] * amount
    return state

#part 1
state = {}
state['x'] = 0
state['y'] = 0 
state['f'] = 'E'
for line_instuction in list_line:
    state = advance_1(state, line_instuction)
dist = abs(state['x']) + abs(state['y'])
print(dist)

#part 2
state = {}
state['x'] = 0
state['y'] = 0 
state['vx'] = 10
state['vy'] = 1 
for line_instuction in list_line:
    state = advance_2(state, line_instuction)
dist = abs(state['x']) + abs(state['y'])
print(dist)