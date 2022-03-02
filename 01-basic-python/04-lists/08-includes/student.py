# Write your code here
def includes(xs, ys):
    for y in ys:
        if not y in xs:
            return False
    return True