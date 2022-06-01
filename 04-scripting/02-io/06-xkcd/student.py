from re import U
import sys, urllib.request, json
from tkinter import W

def fetch_data():
    if(len(sys.argv)==1):
        url="https://xkcd.com/info.0.json"
    else:
        number=sys.argv[1]
        url=f"https://xkcd.com/{number}/info.0.json"
    with urllib.request.urlopen(url) as stream:
        # decode turns way bytes into a string
        data = stream.read().decode('utf-8')

    return json.loads(data)

data = fetch_data()

for key, value in data.items():
    print(f'{key}: {value}')


