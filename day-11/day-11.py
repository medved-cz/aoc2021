#!/usr/bin/env python3

C1 = '\033[92m'
C0 = '\033[0m'

data = 'input'
#data = 'input-test'

print()
print('--- Day 11: Dumbo Octopus ---')
print('Input file is: ' +C1 + str(data) + C0, end = '\n' * 2)

def split(word):
    return list(word)

def printnumbers(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            print(numbers[i][j], end = '')
        print()

def printnumberslong(numbers,lenght):
    print(u'\u2554' + (u'\u2550' * lenght + u'\u2566') * (len(numbers[0]) - 1) + u'\u2550' * lenght + u'\u2557')
    for i in range(len(numbers)):
        print(u'\u2551',end='')
        for j in range(len(numbers[i])):
            print(str('000' + str(numbers[i][j])).rjust(lenght)[-lenght:], end = '')
            print('', end = u'\u2551')
        print()
        if i == len(numbers) - 1:
            break
        print(u'\u2560' + (u'\u2550' * lenght + u'\u256c') * (len(numbers[0]) - 1) + u'\u2550' * lenght + u'\u2563')
    print(u'\u255a' + (u'\u2550' * lenght + u'\u2569') * (len(numbers[0]) - 1) + u'\u2550' * lenght + u'\u255d')

input = open(data, "r")
inputlist = input.readlines()
input.close
lines = len(inputlist)
rows = len(inputlist[0].replace('\n',''))
numbers1 = [0] * lines
numbers2 = [0] * lines
steps = 1000
flashes = 0
flashesold = 0

for x in range(lines):
    numbers1[x] = [int(num) for num in split(inputlist[x].replace('\n',''))]
    numbers2[x] = [0] * rows

for i in range(steps):
    for y in range(lines):
        for x in range(rows):
            numbers1[y][x] += 1
            numbers2[y][x] = 0
    change = True
    while change:
        change = False
        for y in range(lines):
            for x in range(rows):
                if numbers1[y][x] > 9 and numbers2[y][x] == 0:
                    numbers2[y][x] += 1
                    flashes += 1
                    change = True
                    if y - 1 < 0:
                        starty = y
                        stopy = y + 1 + 1
                    elif y + 1 > lines - 1:
                        starty = y - 1
                        stopy = y + 1
                    else:
                        starty = y - 1
                        stopy = y + 1 + 1
                    if x - 1 < 0:
                        startx = x
                        stopx = x + 1 + 1
                    elif x + 1 > rows - 1:
                        startx = x - 1
                        stopx = x + 1
                    else:
                        startx = x - 1
                        stopx = x + 1 + 1
                    for m in range(starty, stopy, 1):
                        for n in range(startx, stopx, 1):
                            if numbers2[m][n] == 0:
                                numbers1[m][n] += 1
                    numbers1[y][x] = 0
    if i == 100:
        print('--- Part One ---')
        print('After ' + C1 + str(i) + C0 + ' steps, there have been a total of ' + C1 + str(flashes) + C0 + ' flashes.', end = '\n' * 2)
    if flashes == flashesold + lines * rows:
        print('--- Part Two ---')
        print('Step ' + C1 + str(i + 1) + C0 + ' is the first step during which all octopuses flash.', end = '\n' * 2)
        break
    flashesold = flashes
