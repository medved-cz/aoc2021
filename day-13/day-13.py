#!/usr/bin/env python3

def formatpaper(x, y):
    paper = []
    for i in range(y):
        paper.append([])
        for j in range(x):
            paper[i].append(0)
    return(paper)

def printpaper(paper):
    for i in range(len(paper)):
        for j in range(len(paper[i])):
            if paper[i][j] == 0:
                print('.', end = '')
            else:
                print('#', end = '')
        print()
    print()

def foldpaper(paper, fold):
    if fold[0] == 'y':
        x = len(paper[0])
        y = fold[1]
        papernew = formatpaper(x, y)
        for i in range(y):
            for j in range(x):
                papernew[i][j] = paper[i][j] + paper[-1 * i - 1][j]
    if fold[0] == 'x':
        x = fold[1]
        y = len(paper)
        papernew = formatpaper(x, y)
        for i in range(y):
            for j in range(x):
                papernew[i][j] = paper[i][j] + paper[i][-1 * j - 1]
    return(papernew)

def countdots(paper):
    count = 0
    for i in range(len(paper)):
        for j in range(len(paper[i])):
            if paper[i][j] > 0:
                count += 1
    return(count)


with open('input') as input:
#with open('input-test') as input:
    lines = input.read().splitlines()
blankline = 0
maxx = 0
maxy = 0
dots = []
folds = []
for i in range(len(lines)):
    if blankline == 0:
        if lines[i + 1] == '':
            blankline = 1 + i
        lines[i] = lines[i].split(',')
        dots.append([])
        dots[i].append(int(lines[i][0]))
        dots[i].append(int(lines[i][1]))
    if i > blankline and blankline > 0:
        lines[i] = lines[i].split()
        lines[i] = lines[i][2]
        lines[i] = lines[i].split('=')
        folds.append([])
        folds[i - blankline - 1].append(lines[i][0])
        folds[i - blankline - 1].append(int(lines[i][1]))
for fold in folds:
    if fold[0] == 'x' and fold[1] > maxx:
        maxx = 2 * fold[1] + 1
    if fold[0] == 'y' and fold[1] > maxy:
        maxy = 2 * fold[1] + 1

paper = formatpaper(maxx, maxy)

for dot in dots:
    paper[dot[1]][dot[0]] = 1

c = 0
for fold in folds:
    paper = foldpaper(paper, fold)
    c += 1
    print('After fold number ' + str(c) + ' there are ' + str(countdots(paper)) + ' dots on paper.')

print()
printpaper(paper)
print('That is paper after last fold.')
