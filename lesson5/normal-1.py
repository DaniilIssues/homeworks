import argparse

parser = argparse.ArgumentParser()
parser.add_argument("N", type=int, help="Num")
parser.add_argument("S", type=str, help="Text")
args = parser.parse_args()
for i in range(args.N):
    print(args.S)