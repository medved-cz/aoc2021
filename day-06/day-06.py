#!/usr/bin/env python3

C1 = '\033[92m'
C0 = '\033[0m'

data = 'input'
#data = 'input-test'

print()
print('--- Day 6: Lanternfish ---')
print('Input file is: ' +C1 + str(data) + C0, end = '\n' * 2)

days = 256
input = open(data, "r")
fishlist = input.readlines()
input.close()
fish = fishlist[0].split(',')
for n in range(len(fish)):
    fish[n] = int(fish[n])

fish0 = fish.count(0)
fish1 = fish.count(1)
fish2 = fish.count(2)
fish3 = fish.count(3)
fish4 = fish.count(4)
fish5 = fish.count(5)
fish6 = fish.count(6)
fish7 = fish.count(7)
fish8 = fish.count(8)
fishx = 0

for day in range(1, days + 1, 1):
    fishx = fish0
    fish0 = fish1
    fish1 = fish2
    fish2 = fish3
    fish3 = fish4
    fish4 = fish5
    fish5 = fish6
    fish6 = fish7 + fishx
    fish7 = fish8
    fish8 = fishx
    if day == 80:
        print('--- Part One ---')
        print('There are ' + C1 + str(fish0+fish1+fish2+fish3+fish4+fish5+fish6+fish7+fish8) + C0 + ' lanternfish after ' + C1 + str(day)  + C0 +' days.', end = '\n' * 2)
print('--- Part Tne ---')
print('There are ' + C1 + str(fish0+fish1+fish2+fish3+fish4+fish5+fish6+fish7+fish8) + C0 + ' lanternfish after ' + C1 + str(day)  + C0 +' days.', end = '\n' * 2)
