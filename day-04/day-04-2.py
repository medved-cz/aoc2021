#!/usr/bin/env python3

input = open("input", "r")
nt = 100
#input = open("input-test", "r")
#nt = 3

lines = input.readlines()
numbers = [int(num) for num in lines[0].split(',')]
tables = [0] * 2 * nt
n = t = bingo = 0
bingot = []

for n in range(nt):
    taba = n
    tabb = n + nt
    tables[taba] = []
    tables[tabb] = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    for i in range(5):
        tables[taba].append([int(num) for num in lines[n*6+2+i].split()])

del lines

for number in numbers:
    n = 0
    t += 1
    for n in range(nt):
        taba = n
        tabb = n + nt
        posx = posy = 0
        for posx in range(5):
            if number in tables[taba][posx]:
                posy = tables[taba][posx].index(number)
                tables[tabb][posx][posy] = 1
    for n in range(nt):
        taba = n
        tabb = n + nt
        pos = 0
        for pos in range(5):
            if tables[tabb][pos][0] + tables[tabb][pos][1] + tables[tabb][pos][2] + tables[tabb][pos][3] + tables[tabb][pos][4] == 5:
                if not taba in bingot:
                    bingot.append(taba)
            if tables[tabb][0][pos] + tables[tabb][1][pos] + tables[tabb][2][pos] + tables[tabb][3][pos] + tables[tabb][4][pos] == 5:
                if not taba in bingot:
                    bingot.append(taba)
            if len(bingot) == nt:
                ct1 = tabsum = 0
                for ct1 in range(5):
                    ct2 = 0
                    for ct2 in range(5):
                        if tables[tabb][ct1][ct2] == 0:
                            tabsum += tables[taba][ct1][ct2]
                print(str(tabsum) + ' * ' + str(number) + ' = ' + str(tabsum * number))
                quit()





