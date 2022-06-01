import argparse

parser = argparse.ArgumentParser()
parser.add_argument("start", help="The start of your range", type=int)
parser.add_argument("end", help="The end of your range", type=int)
parser.add_argument("-x", "--exclusive", help="Exclude end from your range", action="store_true")
parser.add_argument('--step', help="Define the steps of your range", default=1, type=int)

args = parser.parse_args()
print(args)
for i in range(args.start, (args.end if args.exclusive else args.end+1), args.step):
    print(i)