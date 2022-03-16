# Write your code here
import re

def parse_link(string):
    match = re.fullmatch(r'<a href="(.*)">(.*)</a>', string)
    if match:
        l,c=match.groups('')
        return(c,l)
    else: return None
