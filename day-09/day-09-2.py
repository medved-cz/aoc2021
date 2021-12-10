#!/usr/bin/env python3

def split(word):
    return list(word)

def printnumbers(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            num = str(numbers[i][j])
            print(num.rjust(2), end = '')
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
    numbers1[x] = [int(num) for num in split(inputlist[x].replace('\n',''))]
    numbers2[x] = [0] * rows
for y in range(lines):
    for x in range(rows):
        if numbers1[y][x] < 9:
            numbers2[y][x] = numbers1[y][x] + 10
        else:
            numbers2[y][x] = ' '
printnumbers(numbers2)
