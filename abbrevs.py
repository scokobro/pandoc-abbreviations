#!/usr/bin/env python3

"""
Replace all abbreviations defined in file 'dbase' (assumed to be in default '.pandoc' direc), and in document metadata.
Abbreviations in PDmarkdown are marked by a preceding '+'.
In document metadata -> '+abbrev: expansion'.
If an abbreviation cannot be found, it will be marked in output with double exclamation marks '!!'
"""
import sys
import json
import os
from pandocfilters import *

home = os.environ['HOME']
dbasePath = home + '/.pandoc/dbase'# path to abbrev dbase file
#dbasePath = 'a/path/of/your/choice'# user selected path
abbrevlist = {}# create empty dictionary for abbrev=expansion list
f = open(dbasePath, 'r')# open dbase file for reading

# add abbreviations and expansions from dbase file
for line in f:
    dbline = line.strip().split('=')# split each line around the = sign
    abbrevlist[dbline[0]] = dbline[1]# add to abbrev=expansion dictionary

def abbreplace(key, value, format, meta):

    # add abbreviations from file metadata
    for k, v in meta.items():#get keys, values for all metadata
        if k.startswith('+'):# does the key start with a plus sign?
            expan = ''# clear the string which the expansion will be stored in
            for i in range(len(v['c'])):# check all elements in a metadata item
                if v['c'][i]['t'] == 'Space': # if it's type 'space' then add a space to the result
                    expan = expan + " "
                elif 'Str' in v['c'][i]['t']: # if it's a string, add the string
                    expan = expan + v['c'][i]['c']
            abbrevlist[str(k.strip('+'))] = expan # add key and value to the abbrev dictionary

    if key == 'Str' and value.startswith('+'):# is the string an abbrev? (starts with a plus?)
        bare = value.strip('.,;:')# get the bare abbrev string
        punct = value.lstrip(bare)# remove bare string from left leaving any punctuation on right
        if bare.strip('+') in abbrevlist:# check the key(ie abbrev) is defined
            return Str(abbrevlist[bare.strip('+')] + punct)# send back the 'value' of the abbrev 'key', add punct.
        else:# if abbrev is not defined in dbase
            return Str(value + '!!')# send back the original with a warning.

if __name__ == "__main__":
    toJSONFilter(abbreplace)
