#!/usr/bin/env python3

input = open("input", "r")

crablist = input.readlines()
crab = crablist[0].split(',')
for n in range(len(crab)):
    crab[n] = int(crab[n])
crabmin = min(crab)
crabmax = max(crab)
move = [0] * crabmax
n = 1
for n in range(crabmax):
    for c in crab:
        move[n] += abs( c - n )
movemin = min(move)
movenum = move.index(movemin)
print(movemin)
print(movenum)
