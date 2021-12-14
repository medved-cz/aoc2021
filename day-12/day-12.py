#!/usr/bin/env python3

def resetcaves():
    global caveslist
    global caves
    cavesused = {cave : 0 for cave in caveslist}

#with open('input') as input:
with open('input-test') as input:
    connections = input.read().splitlines()
for i in range(len(connections)):
    connections[i] = connections[i].split('-')
caveslist = []
cavesconnections = []
for connection in connections:
    caveslist.append(connection[0])
    caveslist.append(connection[1])
#caveslist = list(dict.fromkeys(caveslist))
for i in range(len(caveslist)):
    cavesconnections.append([])
    for connection in connections:
        if caveslist[i] == connection[0]:
            cavesconnections[i].append(connection[1])
        elif caveslist[i] == connection[1]:
            cavesconnections[i].append(connection[0])
caves = dict.fromkeys(caveslist)
for cave in caves:
    cave = dict(zip(cavesconnections))



print(caves)

quit()
caves = dict(zip(caveslist, cavesconnections))
cavesused = {cave : 0 for cave in caveslist}

for connection1 in cavesconnections[0]:
    path = 'start'






print(caves)
print(cavesused)
