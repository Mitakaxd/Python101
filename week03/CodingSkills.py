import json
import sys
def readJson(filename):
    with open(filename,'r') as f:
        d=json.load(f)
        return d

def main():
    args = sys.argv[1]
    people = readJson(args)["people"]
    skills = {}
    for person in people:
        for skill in person["skills"]:
            if skill["name"] in skills:
                if skill["level"] > skills[skill["name"]][0]:
                    skills[skill["name"]] = (skill["level"],person["first_name"] + person["last_name"])
            else:
                skills[skill["name"]] = (skill['level'],person["first_name"] + person["last_name"])
    for key,value in skills.items():
        print(key,value[1])

if __name__ == '__main__':
    main() 
