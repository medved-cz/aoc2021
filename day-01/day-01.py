#!/usr/bin/env python3

C1 = '\033[92m'
C0 = '\033[0m'

data = 'input'
#data = 'input-test'

print()
print('--- Day 1: Sonar Sweep ---')
print('Input file is: ' + C1 + str(data) + C0, end = '\n' * 2)

with open(data) as input:
    measurements = [int(measurement) for measurement in input.read().splitlines()]

inc = 0

for i in range(1,len(measurements),1):
    if measurements[i] > measurements[i-1]:
        inc += 1

print('--- Part One ---')
print('There are ' +C1 + str(inc) + C0 + ' measurements that are larger than the previous measurement.', end = '\n' * 2)

inc = 0

for i in range(3,len(measurements),1):
    if measurements[i] + measurements[i - 1] + measurements[i - 2] > measurements[i-1] + measurements[i-2] + measurements[i-3]:
        inc += 1

print('--- Part Two ---')
print('There are ' + C1 + str(inc) + C0 + ' sums that are larger than the previous sum.', end = '\n' * 2)
