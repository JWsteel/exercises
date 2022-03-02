# Write your code here
def from_lists(keys, values):
    result={}
    for x in range(len(keys)):
        result[keys[x]]=values[x]
    return result