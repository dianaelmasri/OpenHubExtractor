#!/usr/bin/python
#new
import sys

inputFile = sys.argv[1]
outputFile = sys.argv[2]

with open(inputFile) as result:
    uniqlines = set(result.readlines())
    with open(outputFile, 'w') as rmdup:
        rmdup.writelines(set(uniqlines))