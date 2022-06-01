import re

def match(string):
    return re.fullmatch("^P.*on$", string)