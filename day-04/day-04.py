#!/usr/bin/env python3

C1 = '\033[92m'
C0 = '\033[0m'

data = 'input'
#data = 'input-test'

print()
print('--- Day 4: Giant Squid ---')
print('Input file is: ' + C1 + str(data) + C0, end = '\n' * 2)

input = open(data, "r")
lines = input.readlines()
input.close()
nt = int((len(lines) - 1) / 6)
numbers = [int(num) for num in lines[0].split(',')]
tables = [0] * 2 * nt
bingo = 0
bingot = []
tabsum = []

for n in range(nt):
    taba = n
    tabb = n + nt
    tables[taba] = []
    tables[tabb] = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    for i in range(5):
        tables[taba].append([int(num) for num in lines[n*6+2+i].split()])

del lines

for number in numbers:
    for n in range(nt):
        taba = n
        tabb = n + nt
        posx = posy = 0
        for posx in range(5):
            if number in tables[taba][posx]:
                posy = tables[taba][posx].index(number)
                tables[tabb][posx][posy] = 1
        for pos in range(5):
            bingotold = len(bingot)
            if tables[tabb][pos][0] + tables[tabb][pos][1] + tables[tabb][pos][2] + tables[tabb][pos][3] + tables[tabb][pos][4] == 5:
                if not taba in bingot:
                    bingot.append(taba)
            if tables[tabb][0][pos] + tables[tabb][1][pos] + tables[tabb][2][pos] + tables[tabb][3][pos] + tables[tabb][4][pos] == 5:
                if not taba in bingot:
                    bingot.append(taba)
            if (len(bingot) == 1 and bingotold == 0) or len(bingot) == nt:
                sum = 0
                for ct1 in range(5):
                    for ct2 in range(5):
                        if tables[tabb][ct1][ct2] == 0:
                            sum += tables[taba][ct1][ct2]
                tabsum.append(sum * number)
            if len(bingot) == nt:
                break
        if len(bingot) == nt:
            break
    if len(bingot) == nt:
        break

print('--- Part One ---')
print('Score of the first wining table is: ' + C1 + str(tabsum[0]) + C0, end = '\n' * 2)

print('--- Part Two ---')
print('Score of the last wining table is: ' + C1 + str(tabsum[1]) + C0, end = '\n' * 2)
