import os
import sys
import json

with open('input.txt', 'r') as file:
    list_line = file.readlines()

#part 1
count_correct = 0
for line in list_line:
    count_min = int(line.split(' ')[0].split('-')[0])
    count_max = int(line.split(' ')[0].split('-')[1])
    str_token = line.split(' ')[1][:-1]
    str_password = line.split(' ')[2]
    count_token = str_password.count(str_token)
    if count_min <= count_token and count_token <= count_max:
        count_correct += 1
print(count_correct)


#part 1
count_correct = 0
for line in list_line:
    index_0 = int(line.split(' ')[0].split('-')[0]) - 1
    index_1 = int(line.split(' ')[0].split('-')[1]) - 1
    str_token = line.split(' ')[1][:-1]
    str_password = line.split(' ')[2].rstrip()
    if str_password[index_0] == str_token and str_password[index_1] != str_token:
        count_correct += 1
    elif str_password[index_0] != str_token and str_password[index_1] == str_token:
        count_correct += 1
print(count_correct)