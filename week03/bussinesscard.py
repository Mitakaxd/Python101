import json
import MarkupPy
import sys
#$ python3 solution.py data.json
def makeHtmlforPerson(person):
    



def main(filename):
    with open(filename) as f:
        d = json.load(f)
        return [makeHtmlforPerson(person) for person in d["people"]]

if __name__ == '__main__':
    main(sys.argv[1])