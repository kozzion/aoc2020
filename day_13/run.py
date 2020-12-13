import os
import sys
import numpy as np
import math

with open('input.txt', 'r') as file:
    list_line = file.readlines()
list_line = [line.strip() for line in list_line]

#parse
time_leave = int(list_line[0])
list_time_bus = []
list_time_offset = []
for offset, str_time_bus in enumerate(list_line[1].split(',')):
    if str_time_bus != 'x':
        list_time_bus.append(int(str_time_bus))
        list_time_offset.append(offset)



def find_first_after(time_leave, time_bus):
    time_last = time_leave - (time_leave % time_bus)
    if time_last == time_leave:
        return time_leave
    else:
        return time_last + time_bus

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def merge_bus(peroid_bus_a, offset_a, peroid_bus_b, offset):
    time_a = offset_a
    time_b = (time_a // peroid_bus_b) * peroid_bus_b
    while (time_a + offset != time_b): # this can be sped up a lot with smarter adding
        if time_a + offset < time_b:
            time_a += peroid_bus_a
        else:
            time_b = find_first_after(time_b + 1, peroid_bus_b)
    return lcm(peroid_bus_a, peroid_bus_b), time_a


# part 1
list_time_next = []
for time_bus in list_time_bus:
    list_time_next.append(find_first_after(time_leave, time_bus))

time_min = min(list_time_next)
index_min = np.argmin(list_time_next)

print((time_min - time_leave) * list_time_bus[index_min])

# part 2
period_merged = list_time_bus[0]
offset_merged = 0
for i in range(1, len(list_time_bus)): 
    period_merged, offset_merged = merge_bus(period_merged, offset_merged, list_time_bus[i], list_time_offset[i])
    print('merged')
    print(period_merged)
    print(offset_merged)
    sys.stdout.flush()
print(offset_merged)