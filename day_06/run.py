import os
import sys
import json

with open('input.txt', 'r') as file:
    list_line = file.readlines()
list_line = [line.strip() for line in list_line]


list_list_person = []
list_person = []
for line in list_line:
    if line == '':
        list_list_person.append(list_person)
        list_person = []
    else:
        person = {}
        for char in line:
            person[str(char)] = True
        list_person.append(person)
if 0 < len(list_person):
    list_list_person.append(list_person)
    list_person = []


#part 1
count = 0
for list_person in list_list_person:
    dict_question_yes = {}
    for person in list_person:
        for question in person:
            dict_question_yes[question] = True
    count += len(dict_question_yes)
print(count)


#part 2
count = 0
for index_group, list_person in enumerate(list_list_person):
    dict_count_question_yes = {}
    for person in list_person:
        for question in person:
            if not question in dict_count_question_yes:
                dict_count_question_yes[question] = 0
            dict_count_question_yes[question] += 1
    for question, count_question in dict_count_question_yes.items():
        if count_question == len(list_person):
            count += 1
print(count)