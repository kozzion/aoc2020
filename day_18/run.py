import os
import sys
import numpy as np
from scipy import ndimage

with open('input.txt', 'r') as file:
    list_line = file.readlines()
list_line = [line.strip() for line in list_line]


#parse

class ExpressionValue(object):

    def __init__(self, value):
        self.value = value

    def evaluate_1(self):
        return self.value

    def evaluate_2(self):
        return self.value

class ExpressionComp(object):
    
    def __init__(self, list_token):
        self.list_operant = []
        self.list_operator = []
        while 0 < len(list_token):
            token = list_token.pop(0)
            if token == '(':
                self.list_operant.append(ExpressionComp(list_token))
            elif token == ')':
                break
            elif token == '+':
                self.list_operator.append('+')
            elif token == '*':
                self.list_operator.append('*')
            else:
                self.list_operant.append(ExpressionValue(int(token)))

    def evaluate_1(self):
        value = self.list_operant[0].evaluate_1()
        for index_operant in range(1, len(self.list_operant)):
            if self.list_operator[index_operant -1] == '+':
                value += self.list_operant[index_operant].evaluate_1()        
            elif self.list_operator[index_operant -1] == '*':
      
                value *= self.list_operant[index_operant].evaluate_1()
            else:
                raise Exception()
        return value


    def evaluate_2(self):
        list_value_sum = []
        value_sum = self.list_operant[0].evaluate_2()
        for index_operator, operator in enumerate(self.list_operator):
            if operator == '+':
                value_sum += self.list_operant[index_operator + 1].evaluate_2()
            else:
                list_value_sum.append(value_sum)
                value_sum = self.list_operant[index_operator + 1].evaluate_2()    
        list_value_sum.append(value_sum)

        value = 1
        for value_sum in list_value_sum:
            value *= value_sum
        return value

#parse
list_expresion = []
for line in list_line:
    line = line.replace('(', '( ')
    line = line.replace(')', ' )')
    list_token = line.split(' ') 
    list_expresion.append(ExpressionComp(list_token))
    
# part 1
sum = 0
for expression in list_expresion:
    sum += expression.evaluate_1() 
print(sum)


# part 2
sum = 0
for expression in list_expresion:
    sum += expression.evaluate_2() 
print(sum)