 # Implement an alternative to du -h command
import os
import sys



def sizeof(dirpath):
    mydir =  os.scandir(dirpath)
    size = 0
    for entry in mydir:
        if entry.is_dir():
            size += sizeof(dirpath + "/" + entry.name)
        else:
            fileInfo = os.stat(dirpath + "/" + entry.name)
            size += fileInfo.st_size
    return size
def main():
    args = sys.argv
    print (sizeof(args[1])//1000, "K")


if __name__=='__main__':
    main()
