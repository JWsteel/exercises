# Write your code here
def is_increasing(xs):
    i=0
    while(i+1<len(xs)):
        x=xs[i]
        y=xs[i+1]
        if x>y:
            return False
        i+=1
    
    return True