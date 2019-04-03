#LINUXCOMMANDS
# cat.py
import os
import sys

def cat(file_name):
    with open(file_name,'r+') as file:
        lines=file.readlines()
        for line in lines:
            print(line)

def cat2(args):
    for argument in args:
        cat(argument)




def main():
    cat2(sys.argv[1:])

if __name__ == '__main__':
    main()
