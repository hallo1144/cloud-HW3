#!/usr/bin/env python

import sys

for l in sys.stdin:
    ls = l.strip().split()
    if len(ls) <= 4:
        continue
    
    t = ls[3][1:]
    print(t + " 1")