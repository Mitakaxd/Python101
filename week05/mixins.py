import json
import xml.etree.ElementTree as ET
# <Panda><name>Ivo</name></Panda>

class Xmlable:
    def to_xml(self):
        classname=self.__class__.__name__
        output= ET.Element(classname)
        for k,v in self.__dict__.items():
            newtag=ET.SubElement(output,str(k))
            newtag.text=str(v)
        return ET.tostring(output)
    @classmethod
    def from_xml(cls,xml_string):
        root = ET.fromstring(xml_string)
        classObject=cls()
        for child in root:
            value=child.text
            if child.text.isdigit():
                value=int(child.text)
            setattr(classObject,child.tag,value)
        return classObject  

class Jsonable:
    def to_Json_string(self,indent=4):
        tip=type(self)
        tip=str(tip).split('.')
        tip=tip[-1][:-2]
        d={"type":tip,"dict":self.__dict__}
        string=json.dumps(d,indent=indent)
        return string
    @classmethod
    def from_json(cls,json_string):
        a=cls()
        d= json.loads(json_string)
        for k,v in d["dict"].items():
            setattr(a,k,v)
        return a
class Panda(Jsonable,Xmlable):
    def __eq__(self,other):
        return self.name==other.name and self.years==other.years and self.age==other.age
    def __str__(self):
        return "name : " + self.name + " years: "+str(self.years) + " age: "+ str(self.age)
    def __repr__(self):
        return self.__str__
    def __init__(self, name="Empty",years=0,age=0):
        self.name=name
        self.years=years
        self.age=age








def main():
    p=Panda(name="Ivo",years=15,age=10)
    a=Panda.from_xml(p.to_xml())
    print(a)
    print(p)
    assert a==p
    
    # assert q==p





if __name__ == '__main__':
    main()