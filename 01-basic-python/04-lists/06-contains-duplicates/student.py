# Write your code here
from operator import truediv


def contains_duplicates(array):
    for i in range(0,len(array)):
        for j in range(i+1,len(array)):
            if(array[i]==array[j]):
                return True
    return False