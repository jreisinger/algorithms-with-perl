#!/usr/bin/python
import pprint

def invert_dict(d):
    inverted = {}
    for k, v in d.items():
        if v not in inverted:
            inverted[v] = [k]
        else:
            inverted[v].append(k)
    return inverted

d = { 'one': 1, 'two': 2, 'due': 2, 'three': 3 }

di = invert_dict(d)
pprint.pprint(di)
