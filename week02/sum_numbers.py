import sys



def main():
    args = sys.argv
    with open(args[1]) as f:
        lines = f.readlines()
        sumlst = 0 
        for line in lines:
            sumlst += int(line)
        print(sumlst)

if __name__=='__main__':
    main()