import re

with open('input.txt', 'r') as file:
    with open('output.txt', 'w') as out:
        for line in file:
            line=line.strip()
            match = re.fullmatch( r"(.*:)([0-9]+)/([0-9]+) (.*)", line)
            plus=0
            minus=0
            for str in match.group(4):
                if(str=='+'):
                    plus+=1
                if(str=='-'):
                    minus+=1
            one=int(match.group(2))
            two=int(match.group(3))
            one+=minus
            two+=plus
            out.write(f'{match.group(1)}{one}/{two}\n')