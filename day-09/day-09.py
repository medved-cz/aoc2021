#!/usr/bin/env python3

def split(word):
    return list(word)

def printnumbers(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            print(numbers[i][j], end = '')
        print()
    print()

input = open("input", "r")
#input = open("input-test", "r")

inputlist = input.readlines()
lines = len(inputlist)
rows = len(inputlist[0].replace('\n',''))
numbers1 = [0] * lines
numbers2 = [0] * lines
for x in range(lines):
    #numbers1[x] = split(inputlist[x].replace('\n',''))
    numbers1[x] = [int(num) for num in split(inputlist[x].replace('\n',''))]
    numbers2[x] = [0] * rows
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
            numbers2[y][x] = 1
#printnumbers(numbers2)
risk = 0
for y in range(lines):
    for x in range(rows):
        if numbers2[y][x] == 1:
            risk = risk + 1 + numbers1[y][x]
print(risk)

#print(numbers1)
#print(numbers2)
