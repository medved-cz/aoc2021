#!/usr/bin/env python3

C1 = '\033[92m'
C0 = '\033[0m'

#data = 'input'
data = 'input-test'

print()
print('--- Day 17: Trick Shot ---')
print('Input file is: ' + C1 + str(data) + C0, end = '\n' * 2)

def step():

with open(data) as input:
    ta = input.read()
ta = ta[15:].replace('\n', '')
ta = ta.split(', y=')
ta[0] = [int(num) for num in ta[0].split('..')]
ta[1] = [int(num) for num in ta[1].split('..')]
print(ta)






"""
print('--- Part One ---')
print('There are ' +C1 + str(inc) + C0 + ' measurements that are larger than the previous measurement.', end = '\n' * 2)

print('--- Part Two ---')
print('There are ' + C1 + str(inc) + C0 + ' sums that are larger than the previous sum.', end = '\n' * 2)
"""
