#!/usr/bin/env python3
def printarray():
    global array
    i = 0
    for i in range(len(array)):
        j = 0
        for j in range(len(array[i])):
            print(array[i][j], end = '')
        print()
    print()

input = open("input", "r")
#input = open("input-test", "r")

lines = input.readlines()
numlines = len(lines)
maxx = maxy = i = j = k = ct1 = ct2 = 0
vectors = linesmod = [0] * numlines

for i in range(numlines):
    linesmod[i] = lines[i].replace(' -> ',',')
    vectors[i] = [int(num) for num in linesmod[i].split(',')]
i = 0
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
i = 0
for i in range(maxy + 1):
    array[i] = [0] * (maxx + 1)

for ct1 in range(numlines):
    if vectors[ct1][0] == vectors[ct1][2]:
        if vectors[ct1][1] > vectors[ct1][3]:
            drawy1 = vectors[ct1][3]
            drawy2 = vectors[ct1][1]
        else:
            drawy1 = vectors[ct1][1]
            drawy2 = vectors[ct1][3]
        drawl = drawy2 - drawy1 + 1
        drawx = vectors[ct1][0]
        ct2 = 0
        for ct2 in range(drawl):
            array[drawy1 + ct2][drawx] += 1

    if vectors[ct1][1] == vectors[ct1][3]:
        if vectors[ct1][0] > vectors[ct1][2]:
            drawx1 = vectors[ct1][2]
            drawx2 = vectors[ct1][0]
        else:
            drawx1 = vectors[ct1][0]
            drawx2 = vectors[ct1][2]
        drawl = drawx2 - drawx1 + 1
        drawy = vectors[ct1][1]
        ct2 = 0
        for ct2 in range(drawl):
            array[drawy][drawx1 + ct2] += 1

ct1 = count = 0
for ct1 in range(len(array)):
    ct2 = 0
    for ct2 in range(len(array[ct1])):
        if array[ct1][ct2] > 1:
            count += 1

#printarray()
print(count)
