import os
import sys
from random import randint

def main():
    args = sys.argv
    with open(args[1],'r+') as file:
        for n in range(int(args[2])):
            file.write(str(randint(1,1000)))
            file.write(" ")




if __name__=="__main__":
    main()