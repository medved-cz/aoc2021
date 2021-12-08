#!/usr/bin/env python3

def sort(string):
    return(''.join(sorted(string)))

input = open("input", "r")
#input = open("input-test2", "r")

lines = input.readlines()
numlines = len(lines)
a1 = [''] * numlines
a2 = [''] * numlines
a3 = [''] * numlines
count = 0

for i in range(numlines):
    lines[i] = lines[i].replace('\n','')
    parts = lines[i].split(' | ')
    a1[i] = parts[0]
    a2[i] = parts[1]
    a1[i] = a1[i].split()
    a2[i] = a2[i].split()

for i in range(numlines):
    for j in range(len(a2[i])):
        if len(a2[i][j]) == 2 or len(a2[i][j]) == 3 or len(a2[i][j]) == 4 or len(a2[i][j]) == 7:
            count += 1

def getdigits(codes):
    codes5 = []
    codes6 = []
    digits = [''] * 10
    for x in codes:
        if len(x) == 2:
            digits[1] = x
        elif len(x) == 3:
            digits[7] = x
        elif len(x) == 4:
            digits[4] = x
        elif len(x) == 7:
            digits[8] = x
        elif len(x) == 5:
            codes5.append(x)
        elif len(x) == 6:
            codes6.append(x)

    helpstring = digits[4]
    helpstring = helpstring.replace(digits[1][0],'')
    helpstring = helpstring.replace(digits[1][1],'')

    for x in codes5: # n3
        if digits[1][0] in x and digits[1][1] in x:
            digits[3] = x
            codes5.remove(x)
    for x in codes6: # n9
        if digits[4][0] in x and digits[4][1] in x and digits[4][2] in x and digits[4][3] in x:
            digits[9] = x
            codes6.remove(x)
    for x in codes5: # n5
        if helpstring[0] in x and helpstring[1] in x:
            digits[5] = x
            codes5.remove(x)
    for x in codes6: # n6
        if helpstring[0] in x and helpstring[1] in x:
            digits[6] = x
            codes6.remove(x)

    digits[2] = codes5[0] # n2
    codes5.remove(digits[2])

    digits[0] = codes6[0] # n2
    codes6.remove(digits[0])

    return(digits)

for line in range(len(a1)):
    digits = getdigits(a1[line])
    for pos in range(len(a2[line])):
        for num in range(len(digits)):
            if len(digits[num]) == len(a2[line][pos]):
                if sort(a2[line][pos]) == sort(digits[num]):
                    a3[line] = str(a3[line])+(str(num))

result = 0
for x in a3:
    result += int(x)

print(result)

