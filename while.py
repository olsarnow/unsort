#!/usr/bin/python

with open('xxx', 'r') as f:
  array = []
  for line in f:
    array.append(line)
    print line.rstrip()
f.closed
