#!/usr/bin/env python

import sys

stats = {}

for l in sys.stdin:
    t, c = l.strip().split()
    c = int(c)
    t = t.split(':')[:2]
    ymd = t[0].split('/')
    ymd.reverse()
    t = ymd + [t[1]]
    
    if t[0] not in stats:
        stats[t[0]] = {}
    if t[1] not in stats[t[0]]:
        stats[t[0]][t[1]] = {}
    if t[2] not in stats[t[0]][t[1]]:
        stats[t[0]][t[1]][t[2]] = {}
    if t[3] not in stats[t[0]][t[1]][t[2]]:
        stats[t[0]][t[1]][t[2]][t[3]] = 0
    
    stats[t[0]][t[1]][t[2]][t[3]] += c

for y in sorted(stats.keys()):
    for m in sorted(stats[y].keys()):
        for d in sorted(stats[y][m].keys()):
            for h in sorted(stats[y][m][d].keys()):
                print(y + "-" + m + "-" + d + "-" + h + " " + str(stats[y][m][d][h]))
