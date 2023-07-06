import sys

argumento = sys.argv[1]

with open(argumento, "r") as file:
    print(file.readlines())