# Write your code here
from posixpath import split


def slug(string):
    parts=string.split(' ')
    fname=parts[0]
    lname=parts[1:]
    return '-'.join(s.lower() for s in lname+[fname])