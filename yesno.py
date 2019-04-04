#!/usr/bin/python

yesChoice = ['yes', 'y']
noChoice = ['no', 'n']

input = raw_input("Would you like to play again? (y/N) ").lower()

if input in yesChoice:
    print "ja"
elif input in noChoice:
    print "nein"
    exit (0)
else: 
    print "Enter Yes or No\n"
    exit (1)
