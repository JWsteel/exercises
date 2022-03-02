# Write your code here
def rotate(array, n):
    for x in range (0,n):
        array.append(array.pop(0))