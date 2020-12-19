import os
import sys
import numpy as np
from scipy import ndimage

with open('input.txt', 'r') as file:
    list_line = file.readlines()
list_line = [line.strip() for line in list_line]

class RuleOption(object):
    def __init__(self, id_rule, dict_rule, list_list_id_rule):
        self.id_rule = id_rule
        self.dict_rule = dict_rule
        self.list_list_id_rule = list_list_id_rule
        self.lenght_rule = 0

    def match(self, string, index_string):
        if  len(string) <= index_string:
            return []
        # print('match')
        # print(self.id_rule)
        list_index_string = []
        for list_id_rule in self.list_list_id_rule:
            # print('list_id_rule')
            # print(list_id_rule)
            list_index_string_rule = [index_string]
            list_index_string_rule_next = []
            for id_rule in list_id_rule:
                for index_string_rule in list_index_string_rule:
                    list_index_string_rule_next.extend(self.dict_rule[id_rule].match(string, index_string_rule))
                list_index_string_rule = list_index_string_rule_next
                list_index_string_rule_next = []
            list_index_string.extend(list_index_string_rule) 
        return list_index_string

class RuleValue(object):

    def __init__(self, id_rule, value):
        self.value = value

    def match(self, string, index_string):
        if  len(string) <= index_string:
            return []
        if string[index_string] != self.value:
            return []
        else:
            return [index_string + 1] 

#parse
dict_rule = {}
list_string = []
index_line = 0

while index_line < len(list_line):
    line = list_line[index_line]
    index_line += 1
    if line == '':
        break
    id_rule = line.split(': ')[0]
    if '"' in line.split(': ')[1]:
        value = line.split(': ')[1][-2:-1]
        dict_rule[id_rule] = RuleValue(id_rule, value)
    else:
        list_list_id_rule = []
        for str_option in line.split(': ')[1].split(' | '):
            list_list_id_rule.append(str_option.split(' '))
            dict_rule[id_rule] = RuleOption(id_rule, dict_rule, list_list_id_rule)

while index_line < len(list_line):
    line = list_line[index_line]
    index_line += 1
    list_string.append(line)

# part 1
count = 0
for string in list_string:
    list_index_string = dict_rule['0'].match(string, 0)
    for index_string in list_index_string:
        if index_string == len(string):
            count += 1
            break
print(count)


# # part 2
rule_8b = RuleOption('8', dict_rule, [['42'], ['42', '8']])
rule_11b = RuleOption('11', dict_rule, [['42', '31'], ['42', '11', '31']])
dict_rule[rule_8b.id_rule] = rule_8b
dict_rule[rule_11b.id_rule] = rule_11b

count = 0
for string in list_string:
    list_index_string = dict_rule['0'].match(string, 0)
    for index_string in list_index_string:
        if index_string == len(string):
            count += 1
            break
print(count)
