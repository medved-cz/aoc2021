#!/usr/bin/env python3

#with input as file:
#    while (line := file.readline().rstrip()):
#        print(line)

#ith open('input1', 'r') as file:
#    while (line := file.readline().rstrip()):
#        print(line)

#with open('input1', 'r') as f:
#    numbers = [[int(num) for num in line.split(',')] for line in f if line.strip() != "" ]
#print(numbers)

#with open('input3', 'r') as f:
#    table1 = [[int(num) for num in line.split()] for line in f if line.strip() != "" ]
#print(table1)

input = open("input", "r")

lines=input.readlines()

numbers = lines[0].split(',')
for n in range(len(numbers)):
    numbers[n] = int(numbers[n])

print(numbers)
