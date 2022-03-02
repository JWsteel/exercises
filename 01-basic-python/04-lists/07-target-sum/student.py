def target_sum(array, target):
    for x in array:
        for y in array:
            if x+y==target:
                return True
    return False
