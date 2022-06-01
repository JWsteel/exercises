import csv

with open('solutions.csv') as solutions:
    with open('answers.csv') as answers:
        with open('output.txt', 'w') as out:
            sol_reader = csv.reader(solutions, delimiter=',')
            ans_reader = csv.reader(answers, delimiter=',')
            for line in sol_reader:
                for lines in ans_reader:
                    score=0
                    name=lines[0]
                    for i in range(1,len(lines)):
                        if lines[i]==line[i-1]:
                            score+=1
                    out.write(f'{name} {score}\n')
                