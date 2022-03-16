import sys

inFile = open(sys.argv[1], "r")
outFile= open(sys.argv[2], "w")
outFile.write(inFile.read())
