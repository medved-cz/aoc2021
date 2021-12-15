#!/usr/bin/env python3

import copy

C1 = '\033[92m'
C0 = '\033[0m'

data = 'input'
#data = 'input-test'

print()
print('--- Day 3: Binary Diagnostic ---')
print('Input file is: ' + C1 + str(data) + C0, end = '\n' * 2)

with open(data) as input:
    numbers = input.read().splitlines()

gamma = ''
epsilon = ''
ones = 0
zeroes = 0

for j in range(len(numbers[0])):
    for i in range(len(numbers)):
        if numbers[i][j] == '0':
            zeroes += 1
        else:
            ones += 1
    if ones > zeroes:
        gamma = gamma + '1'
        epsilon = epsilon + '0'
    else:
        gamma = gamma + '0'
        epsilon = epsilon + '1'
    ones = 0
    zeroes = 0

print('--- Part One ---')
print('Power consumption is: ' + C1 + str(int(gamma, 2) * int(epsilon, 2)) + C0, end = '\n' * 2)

oxygen = copy.deepcopy(numbers)
co2 = copy.deepcopy(numbers)

for j in range(len(oxygen[0])):
    ones = 0
    zeroes = 0
    for i in range(len(oxygen)):
        if oxygen[i][j] == '0':
            zeroes += 1
        elif oxygen[i][j] == '1':
            ones += 1
    if ones >= zeroes:
        for k in range(len(oxygen)):
            if oxygen[k][j] == '0':
                oxygen[k] = 'X' * len(oxygen[0])
    if ones < zeroes:
        for k in range(len(oxygen)):
            if oxygen[k][j] == '1':
                oxygen[k] = 'X' * len(oxygen[0])
    oxygen = list(dict.fromkeys(oxygen))
    try:
        oxygen.remove('X' * len(oxygen[0]))
    except:
        True
    if len(oxygen) == 1:
        oxygen = oxygen[0]
        break

for j in range(len(co2[0])):
    ones = 0
    zeroes = 0
    for i in range(len(co2)):
        if co2[i][j] == '0':
            zeroes += 1
        elif co2[i][j] == '1':
            ones += 1
    if ones < zeroes:
        for k in range(len(co2)):
            if co2[k][j] == '0':
                co2[k] = 'X' * len(co2[0])
    if ones >= zeroes:
        for k in range(len(co2)):
            if co2[k][j] == '1':
                co2[k] = 'X' * len(co2[0])
    co2 = list(dict.fromkeys(co2))
    try:
        co2.remove('X' * len(co2[0]))
    except:
        True
    if len(co2) == 1:
        co2 = co2[0]
        break

print('--- Part Two ---')
print('Life support rating is: ' + C1 + str(int(oxygen, 2) * int(co2, 2)) + C0, end = '\n' * 2)
