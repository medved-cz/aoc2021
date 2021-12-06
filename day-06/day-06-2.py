#!/usr/bin/env python3

days = 256
day = 1
input = open("input", "r")

fishlist = input.readlines()

fish = fishlist[0].split(',')
for n in range(len(fish)):
    fish[n] = int(fish[n])

print(fish)

fish0 = fish.count(0)
fish1 = fish.count(1)
fish2 = fish.count(2)
fish3 = fish.count(3)
fish4 = fish.count(4)
fish5 = fish.count(5)
fish6 = fish.count(6)
fish7 = fish.count(7)
fish8 = fish.count(8)
fish9 = fish.count(8)

fishx = 0

print(fish0+fish1+fish2+fish3+fish4+fish5+fish6+fish7+fish8)

for day in range(days):
    fishx = fish0
    fish0 = fish1
    fish1 = fish2
    fish2 = fish3
    fish3 = fish4
    fish4 = fish5
    fish5 = fish6
    fish6 = fish7 + fishx
    fish7 = fish8
    fish8 = fish9
    fish9 = fish0

print(fish0+fish1+fish2+fish3+fish4+fish5+fish6+fish7+fish8)
