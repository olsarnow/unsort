#!/usr/bin/python

with open('xxx', 'r') as f:
  array = []
  for line in f:
    array.append(line)
    print "erste zeile mit", line.rstrip()
    print "zweite zeile mit", line.rstrip()
f.closed
