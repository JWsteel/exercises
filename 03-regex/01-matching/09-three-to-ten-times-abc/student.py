# Write your code here
from re import fullmatch


def three_to_ten_times_abc(string):
    return fullmatch('(abc){3,10}', string)