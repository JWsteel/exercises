# Write your code here
from cgitb import reset


def remove_duplicates(xs):
    result=[]
    xset=set()
    for x in xs:
        if(x not in xset):
            result.append(x)
            xset.add(x)
    return result