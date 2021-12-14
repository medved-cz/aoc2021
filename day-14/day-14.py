#!/usr/bin/env python3

import copy

def getpairs(polymer):
    pairs = []
    length = len(polymer)
    for i in range(1,length,1):
        pair = polymer[i - 1] + polymer[i]
        pairs.append(pair)
    return(pairs)

def resetpairs(pairs):
    for i in range(len(pairs)):
        pairs[i][1] = 0
    return(pairs)

with open('input') as input:
#with open('input-test') as input:
    pairins = input.read().splitlines()

polymer = pairins[0]
pairins.pop(1)
pairins.pop(0)
pairs = []
chars = []
count = []
for i in range(len(pairins)):
    pairins[i] = pairins[i].split(' -> ')
    pairs.append([])
    pairs[i].append([])
    pairs[i][0] = pairins[i][0]
    pairs[i].append(0)
    pairs[i].append(pairins[i][0][0] + pairins[i][1])
    pairs[i].append(pairins[i][1] + pairins[i][0][1])
    pairs[i].append(pairins[i][1])

for pair in getpairs(polymer):
    for i in range(len(pairs)):
        if pairs[i][0] == pair:
            pairs[i][1] += 1
            break
for pair in pairins:
    chars.append(pair[1])
chars = list(dict.fromkeys(chars))

for char in chars:
    count.append(polymer.count(char))

steps = 40
for i in range(1,steps + 1):
    pairsnew = copy.deepcopy(pairs)
    pairsnew = resetpairs(pairsnew)
    for p1 in range(len(pairs)):
        if pairs[p1][1] > 0:
            for p2 in range(len(pairs)):
                if pairs[p2][0] == pairs[p1][2]:
                    pairsnew[p2][1] += pairs[p1][1]
                elif pairs[p2][0] == pairs[p1][3]:
                    pairsnew[p2][1] += pairs[p1][1]
            for j in range(len(chars)):
                if pairs[p1][4] == chars[j]:
                    count[j] += pairs[p1][1]

    pairs = copy.deepcopy(pairsnew)
    if i == 10:
        value = max(count) - min(count)
        print('--- Part One ---')
        print('Answer is: ' + str(value))
        print()

value = max(count) - min(count)
print('--- Part Two ---')
print('Answer is: ' + str(value))
