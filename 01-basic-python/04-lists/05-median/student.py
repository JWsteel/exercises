# Write your code here
def median(array):
    arraySorted=sorted(array)
    i=len(arraySorted)//2
    if len(arraySorted)%2==0: return (arraySorted[i-1]+arraySorted[i])/2
    return arraySorted[i]