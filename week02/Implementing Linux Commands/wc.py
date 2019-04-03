import os
import sys




def main():
    args=sys.argv
    with open(args[1]) as file:
        lines = file.readlines()
        if args[2] == 'lines':
            print(len(lines))
        elif args[2] == "words":
            words = []
            for sentence in lines:
                splitsentence = sentence.split(" ")
                for word in splitsentence:
                    words.append(word)
            print(len(words))
        else:
            count = 0
            for line in lines:
                count += len(lines)
            print(count)


if __name__=="__main__":
    main()