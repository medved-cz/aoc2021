#!/usr/bin/env python3

def printlist(list):
    for i in range(len(list)):
        print(str(i).rjust(3) + ': ' + list[i])
    print()

input = open("input", "r")
#input = open("input-test", "r")

chunks = input.readlines()
incomplete = [''] * len(chunks)
errors = [''] * len(chunks)
for n in range(len(chunks)):
    chunks[n] = chunks[n].replace('\n','')
ch = [['']] * 4
ch[0] = ['(',')',3,1]
ch[1] = ['[',']',57,2]
ch[2] = ['{','}',1197,3]
ch[3] = ['<','>',25137,4]

expected = ''

for x in range(len(chunks)):
    chunk = chunks[x]
    for y in range(len(chunk)):
        for z in range(len(ch)):
            if chunk[y] == ch[z][0]:
                expected += ch[z][1]
                error = 0
                break
            elif chunk[y] == ch[z][1] and ch[z][1] == expected[-1]:
                expected = expected[:-1]
                error = 0
                break
            else:
                error = 1
        if error != 0:
            errors[x] = chunk[y]
            expected = ''
            break
    if expected != '':
        incomplete[x] = expected
        expected = ''

value = 0

for line in errors:
    if line != '':
        for c in range(len(ch)):
            if line == ch[c][1]:
                value += ch[c][2]

print(value)

value = 0
list = []

for line in incomplete:
    if line != '':
        for l in range(len(line)):
            for c in range(len(ch)):
                if line[-(l+1)] == ch[c][1]:
                    value = value * 5 + ch[c][3]
        list.append(value)
        value = 0
list.sort()

print(list[int(len(list)/2)])








