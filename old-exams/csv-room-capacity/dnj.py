import csv

with open('exam-schedule.csv', newline='') as file:
    lmao = csv.reader(file)
    scheduling = []
    for row in lmao:
        relevant=[row[3], row[4],row[5], row[12]]
        if relevant not in scheduling:
            scheduling.append(relevant)
    for row in scheduling:
        print(row)