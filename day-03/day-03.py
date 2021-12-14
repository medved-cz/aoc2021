#!/usr/bin/env python3

with open('input') as input:
#with open('input-test') as input:
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
print('Power consumption is: ' + str(int(gamma, 2) * int(epsilon, 2)))
print()

ones = 0
zeroes = 0
oxygen = numbers
co2 = numbers

for j in range(len(oxygen[0])):
    for i in range(len(oxygen)):
        if oxygen[i][j] == '0':
            zeroes += 1
        else:
            ones += 1
    if ones >= zeroes:
        oxygenold = oxygen
        for k in range(len(oxygen)):
            if oxygenold[k][j] == '0':
                oxygen[k] = ''
    if ones < zeroes:
        oxygenold = oxygen
        for k in range(len(oxygen)):
            if oxygenold[k][j] != '0':
                oxygen[k] = ''

print(oxygen)





quit()
print('--- Part Two ---')
print('Life support rating is: ' + str(horizontal * depth))
