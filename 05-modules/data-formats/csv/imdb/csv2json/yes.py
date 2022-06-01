import sys
import json
import csv

array=[]

with open('E:/Scripttalen/scripting-exercises/05-modules/data-formats/csv/imdb/csv.csv', newline='') as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        array.append(row)
with open('json.json', 'w') as jsonfile:
    jsonfile.write(json.dumps(array))