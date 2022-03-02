# Write your code here
def add_indices(xs):
    list2 = []
    i=0
    while(i<len(xs)):
        list2.append(i)
        i+=1
    return list(zip(list2, xs))