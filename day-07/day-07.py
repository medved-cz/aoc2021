#!/usr/bin/env python3

import statistics

C1 = '\033[92m'
C0 = '\033[0m'

data = 'input'
#data = 'input-test'

print()
print('--- Day 7: The Treachery of Whales ---')
print('Input file is: ' +C1 + str(data) + C0, end = '\n' * 2)

input = open(data, "r")

crablist = input.readlines()
input.close()
crab = crablist[0].split(',')
for n in range(len(crab)):
    crab[n] = int(crab[n])
crabmin = min(crab)
crabmax = max(crab)
pos = int(statistics.median(crab))
movemin = 0

for c in crab:
    movemin += abs(c - pos)

print('--- Part One ---')
print('Fuel cost is: ' + C1 + str(movemin) + C0, end = '\n' * 2)

movecosts = [None] * (crabmax - crabmin)

for n in range(crabmin, crabmax, 1):
    a = 0
    for m in range(crabmin, n):
        a += 1 + m
    movecosts[n] = a
movemin = movecosts[-1] * crabmax
for n in range(crabmin, crabmax - 1, 1):
    move = 0
    for c in crab:
        movec = abs(c - n - 1)
        move += movecosts[movec]
    if move < movemin:
        movemin = move
    else:
        break

print('--- Part Two ---')
print('Fuel cost is: ' + C1 + str(movemin) + C0, end = '\n' * 2)
