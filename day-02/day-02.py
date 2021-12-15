#!/usr/bin/env python3

C1 = '\033[92m'
C0 = '\033[0m'

data = 'input'
#data = 'input-test'

print()
print('--- Day 2: Dive! ---')
print('Input file is: ' +C1 + str(data) + C0, end = '\n' * 2)

with open(data) as input:
    commands = input.read().splitlines()
for i in range(len(commands)):
    commands[i] = commands[i].split()
    commands[i][1] = int(commands[i][1])

horizontal = 0
depth = 0

for command in commands:
    if command[0] == 'forward':
        horizontal += command[1]
    elif command[0] == 'down':
        depth += command[1]
    else:
        depth -= command[1]

print('--- Part One ---')
print('Answer is: ' + C1 + str(horizontal * depth) + C0, end = '\n' * 2)

horizontal = 0
depth = 0
aim = 0

for command in commands:
    if command[0] == 'forward':
        horizontal += command[1]
        depth += command[1] * aim
    elif command[0] == 'down':
        aim += command[1]
    else:
        aim -= command[1]

print('--- Part Two ---')
print('Answer is: ' + C1 + str(horizontal * depth) + C0, end = '\n' * 2)
