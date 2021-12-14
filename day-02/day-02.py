#!/usr/bin/env python3

with open('input') as input:
#with open('input-test') as input:
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
print('Answer is: ' + str(horizontal * depth))
print()

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
print('Answer is: ' + str(horizontal * depth))
