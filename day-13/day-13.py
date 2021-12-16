#!/usr/bin/env python3

C1 = '\033[92m'
C0 = '\033[0m'

data = 'input'
#data = 'input-test'

print()
print('--- Day 13: Transparent Origami ---')
print('Input file is: ' +C1 + str(data) + C0, end = '\n' * 2)

def formatpaper(x, y):
    paper = []
    for i in range(y):
        paper.append([])
        for j in range(x):
            paper[i].append(0)
    return(paper)

def printpaper(paper):
    print(C1, end = '')
    for i in range(len(paper)):
        for j in range(len(paper[i])):
            if paper[i][j] == 0:
                print('.', end = '')
            else:
                print('#', end = '')
        print()
    print(C0)

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


with open(data) as input:
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
    if c ==1:
        print('--- Part One ---')
        print('There are ' + C1 + str(countdots(paper)) + C0 + ' dots on paper after first fold.', end = '\n' * 2)

print('--- Part Two ---', end = '\n' * 2)
printpaper(paper)
print('That is paper after last fold.', end = '\n' * 2)
