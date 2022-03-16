import sys
import urllib.request
import re
import json

artist = sys.argv[1]
title = sys.argv[2]
artist = re.sub(' ', '%20', artist)
title = re.sub(' ', '%20', title)

url = 'https://api.lyrics.ovh/v1/{}/{}'.format(artist, title)

with urllib.request.urlopen(url) as input:
    obj = json.loads(input.read())
    print(obj["lyrics"])
