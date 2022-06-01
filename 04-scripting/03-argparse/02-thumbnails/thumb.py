import argparse
import re
from pathlib import Path

def outname(string, pattern):
    name=string.stem
    suf=string.suffix
    return pattern.replace('%b', name).replace('.%x', suf)

parser = argparse.ArgumentParser()
parser.add_argument("--size", help="The size of the images", default="64x64")
parser.add_argument("--pattern", help="the pattern that is present in the filename please inclue %b and %x", default="%b-thumbnail.%x")
parser.add_argument("files", help="the files you want to thumbnail", nargs="*")

args=parser.parse_args()
print(args)

match=re.fullmatch(r'(\d+)x(\d+)',args.size)
if not match:
    print("no match")
w,h=match.groups()
print(w)
print(h)
for file in args.files:
    string = Path(file)
    print(outname(string, args.pattern))