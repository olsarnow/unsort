#!/usr/bin/python

def yes_or_no():
  yesChoice = ['yes', 'y']
  noChoice = ['no', 'n']

  input = raw_input("question? (y/N) ").lower()

  if input in yesChoice:
    print "ja"
  elif input in noChoice:
    print "nein"
    exit (0)
  else: 
    print "Enter Yes or No\n"
    exit (1)

yes_or_no()
