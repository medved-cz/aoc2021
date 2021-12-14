#!/usr/bin/env python3

with open('input') as input:
#with open('input-test') as input:
    measurements = [int(measurement) for measurement in input.read().splitlines()]

inc = 0

for i in range(1,len(measurements),1):
    if measurements[i] > measurements[i-1]:
        inc += 1

print('--- Part One ---')
print('There are ' + str(inc) + ' measurements that are larger than the previous measurement.')
print()

inc = 0

for i in range(3,len(measurements),1):
    if measurements[i] + measurements[i - 1] + measurements[i - 2] > measurements[i-1] + measurements[i-2] + measurements[i-3]:
        inc += 1

print('--- Part Two ---')
print('There are ' + str(inc) + ' sums that are larger than the previous sum.')
