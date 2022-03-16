import urllib.request, sys

with urllib.request.urlopen(sys.argv[1]) as input:
    webContent = input.read()
    f = open('dammit.txt', 'w')
    f.write(webContent)
    f.close