with open('output.txt', 'w') as out:
    for i in range (1000000):
        out.write(f'{i+1}\n')