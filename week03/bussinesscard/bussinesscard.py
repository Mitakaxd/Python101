import json
import MarkupPy
import sys
#$ python3 solution.py data.json
def makeHtmlforPerson(person):
    items = ( "Item one", "Item two", "Item three", "Item four" )
    paras = ( "This was a fantastic list.", "And now for something completely different." )
    images = ( "thumb1.jpg", "thumb2.jpg", "more.jpg", "more2.jpg" )

    page = MarkupPy.Page( )
    page.init( title=person["first_name"], 
               css=( 'styles.css' ), 
               header="BussinessCard", 
               footer="END" )

    page.ul( class_=person["first_name"] )
    page.li( person["skills"], class_='skill' )
    page.ul.close( )

    page.p( paras )
    page.img( src="/avatars/"+person["first_name"], width=100, height=80, alt="Thumbnails" )

    print(page)



def main(filename):
    with open(filename) as f:
        d=json.load(f)
        return [makeHtmlforPerson(person) for person in d["people"]]

if __name__ == '__main__':
    main(sys.argv[1])