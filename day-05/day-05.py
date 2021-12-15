#!/usr/bin/env python3

C1 = '\033[92m'
C0 = '\033[0m'

data = 'input'
#data = 'input-test'

print()
print('--- Day 5: Hydrothermal Venture ---')
print('Input file is: ' +C1 + str(data) + C0, end = '\n' * 2)

def printarray():
    global array
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(array[i][j], end = '')
        print()
    print()

input = open(data, "r")

lines = input.readlines()
input.close()
numlines = len(lines)
maxx = maxy = 0
vectors = linesmod = [0] * numlines
counts = []
for i in range(numlines):
    linesmod[i] = lines[i].replace(' -> ',',')
    vectors[i] = [int(num) for num in linesmod[i].split(',')]

for i in range(numlines):
    if vectors[i][0] > maxx:
        maxx = vectors[i][0]
    if vectors[i][2] > maxx:
        maxx = vectors[i][2]
    if vectors[i][1] > maxy:
        maxy = vectors[i][1]
    if vectors[i][3] > maxy:
        maxy = vectors[i][3]

array = [0] * ( maxy + 1)

for i in range(maxy + 1):
    array[i] = [0] * (maxx + 1)

for i in range(2):
    count = 0
    for ct1 in range(numlines):
        x1 = vectors[ct1][0]
        x2 = vectors[ct1][2]
        y1 = vectors[ct1][1]
        y2 = vectors[ct1][3]

        if x1 == x2 and i == 0:
            if y1 > y2:
                drawy1 = y2
                drawy2 = y1
            else:
                drawy1 = y1
                drawy2 = y2
            drawl = drawy2 - drawy1 + 1
            drawx = x1
            for ct2 in range(drawl):
                array[drawy1 + ct2][drawx] += 1
        elif y1 == y2 and i == 0:
            if x1 > x2:
                drawx1 = x2
                drawx2 = x1
            else:
                drawx1 = x1
                drawx2 = x2
            drawl = drawx2 - drawx1 + 1
            drawy = y1
            for ct2 in range(drawl):
                array[drawy][drawx1 + ct2] += 1
        elif x1 != x2 and y1 != y2 and i == 1:
            drawx = x2 - x1
            drawy = y2 - y1
            if drawx > 0:
                stepx = 1
            else:
                stepx = -1
            if drawy > 0:
                stepy = 1
            else:
                stepy = -1

            for ct2 in range(abs(drawx) + 1):
                array[y1 + stepy * ct2][x1 + stepx * ct2] += 1

    for ct1 in range(len(array)):
        ct2 = 0
        for ct2 in range(len(array[ct1])):
            if array[ct1][ct2] > 1:
                count += 1
    counts.append(count)

print('--- Part One ---')
print('Sum of all overlaps: ' + C1 + str(counts[0]) + C0, end = '\n' * 2)

print('--- Part Two ---')
print('Sum of all overlaps: ' + C1 + str(counts[1]) + C0, end = '\n' * 2)
