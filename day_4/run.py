import os
import sys
import json

with open('input.txt', 'r') as file:
    list_line = file.readlines()
list_line = [line.strip() for line in list_line]


list_passport = []
passport = {}
for line in list_line:
    if line == '':
        list_passport.append(passport)
        passport = {}
    else:
        list_part = line.split(' ')
        for part in list_part:
            passport[part.split(':')[0]] = part.split(':')[1]
if 0 < len(passport):
    list_passport.append(passport)
    passport = {}


def is_passport_valid(passport):
    list_key_required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl' , 'ecl', 'pid']
    for key_required in list_key_required:
        if not key_required in passport:
            return False
    return True

def is_passport_very_valid(passport):
    if not is_passport_valid(passport):
        return False
    try:
        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        if int(passport['byr']) < 1920 or 2002 < int(passport['byr']) :
            return False
        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        if int(passport['iyr']) < 2010 or 2020 < int(passport['iyr']) :
            return False
        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        if int(passport['eyr']) < 2020 or 2030 < int(passport['eyr']) :
            return False

        # hgt (Height) - a number followed by either cm or in:
        # If cm, the number must be at least 150 and at most 193.
        # If in, the number must be at least 59 and at most 76.
        type_hgt = passport['hgt'][-2:]
        value_hgt = int(passport['hgt'][:-2])        
        if type_hgt == 'cm':
            if value_hgt < 150 or 193 < value_hgt:
                return False
        elif type_hgt == 'in':
            if value_hgt < 59 or 76 < value_hgt:
                return False
        else:
            return False
        
        #hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        if not len(passport['hcl']) == 7:
            return False
        if not passport['hcl'][0] == '#':
            return False
        int(passport['hcl'][1:], 16)

        #ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        if not passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return False
            
        #pid (Passport ID) - a nine-digit number, including leading zeroes.
        if not len(passport['pid']) == 9:
            return False
        if not passport['pid'].isnumeric():
            return False        
    except Exception:
        return False
    return True  


# part 1
count_valid = 0
for index, passport in enumerate(list_passport):
    if is_passport_valid(passport):
        count_valid += 1
print(count_valid)

# part 2
count_valid = 0
for index, passport in enumerate(list_passport):
    if is_passport_very_valid(passport):
        count_valid += 1
print(count_valid)