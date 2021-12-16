#!/usr/bin/env python3

C1 = '\033[92m'
C0 = '\033[0m'

data = 'input'
#data = 'input-test'

print()
print('--- Day 9: Smoke Basin ---')
print('Input file is: ' +C1 + str(data) + C0, end = '\n' * 2)

def split(word):
    return list(word)

def printnumbers(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            print(numbers[i][j], end = '')
        print()
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
numbers3 = [-1] * lines
counter = 0
for x in range(lines):
    numbers1[x] = [int(num) for num in split(inputlist[x].replace('\n',''))]
    numbers2[x] = [0] * rows
    numbers3[x] = [None] * rows
for y in range(lines):
    for x in range(rows):
        p = 3
        values = [10] * p
        for n in range(p):
            values[n] = [9] * 3
        values[1][1] = numbers1[y][x]
        if y-1 >= 0:
            values[0][1] = numbers1[y-1][x]
        if y+1 <= lines - 1:
            values[2][1] = numbers1[y+1][x]
        if x-1 >= 0:
            values[1][0] = numbers1[y][x-1]
        if x+1 <= rows - 1:
            values[1][2] = numbers1[y][x+1]
        if values[0][1] > values[1][1] and values[2][1] > values[1][1] and  values[1][0] > values[1][1] and values[1][2] > values[1][1]:
            counter += 1
            numbers2[y][x] = counter
            numbers3[y][x] = counter - 1

risk = 0
for y in range(lines):
    for x in range(rows):
        if numbers2[y][x] >= 1:
            risk = risk + 1 + numbers1[y][x]

print('--- Part One ---')
print('Answer is: ' + C1 + str(risk) + C0, end = '\n' * 2)

change = True
basins = [1] * counter
while change:
    change = False
    for i in range(counter):
        for y in range(lines):
            for x in range(rows):
                if numbers3[y][x] == i:
                    basinold = basins[i]
                    if y-1 >= 0:
                        if numbers1[y-1][x] < 9 and numbers3[y-1][x] != i:
                            numbers3[y-1][x] = i
                            basins[i] += 1
                            change = True
                    if y+1 <= lines - 1:
                        if numbers1[y+1][x] < 9 and numbers3[y+1][x] != i:
                            numbers3[y+1][x] = i
                            basins[i] += 1
                            change = True
                    if x-1 >= 0:
                        if numbers1[y][x-1] < 9 and numbers3[y][x-1] != i:
                            numbers3[y][x-1] = i
                            basins[i] += 1
                            change = True
                    if x+1 <= rows - 1:
                        if numbers1[y][x+1] < 9 and numbers3[y][x+1] != i:
                            numbers3[y][x+1] = i
                            basins[i] += 1
                            change = True
basins.sort(reverse=True)

print('--- Part Two ---')
print('Answer is: ' + C1 + str(basins[0]*basins[1]*basins[2]) + C0, end = '\n' * 2)
