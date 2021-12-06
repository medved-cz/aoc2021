#!/usr/bin/env python3

days = 256
day = 1
input = open("input-test", "r")

fishlist = input.readlines()

fish = fishlist[0].split(',')
for n in range(len(fish)):
    fish[n] = int(fish[n])

print(fish)
for day in range(days):
    for n in range(len(fish)):
        if fish[n] == 0:
            fish[n] = 7
            fish.append(8)
        if day < days:
            fish[n] -= 1

print(len(fish))
#print(fish)
