with open('input.txt', 'r') as input:
    with open('output.txt', 'w') as output:
        granted=100
        result={}
        for row in input:
            name=row.strip()
            if(granted<1):
                granted=100
            if name not in result:
                result[name]=granted
            else:
                result[name]+=granted
            granted-=1
        for i in range(10):
            value=max(result, key=result.get)
            output.write(f'{value}\n')
            result.pop(value)            
