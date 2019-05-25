import json
import xml.etree.ElementTree as ET
# <Panda><name>Ivo</name></Panda>
from collections import Iterable


class Xmlable:
    pass
#     def to_xml(self):

#         classname = self.__class__.__name__
#         output = ET.Element(classname)
#         def to_xml_helper(dictionary):
#             for k, v in dictionary.items():
#                 newtag = ET.SubElement(output, str(k))
#                     if isinstance(v,Iterable):
#                         newtag.text = to_xml_helper(v)
#                     else:
#                         newtag.text = str(v)
#             return ET.tostring(output)

#     @classmethod
#     def from_xml(cls, xml_string):
#         root = ET.fromstring(xml_string)
#         classObject = cls()
#         for child in root:
#             value = child.text
#             if isinstance(child.tag,Iterable):
#                 value = from_xml(type(child.tag),child.text)
#             if child.text.isdigit():
# .0                      value = int(child.text)
#             setattr(classObject, child.tag, value)
#         return classObject


class Jsonable:
#done
    def to_Json_string(self, indent=4):
        d = self.make_dict(indent=4)
        string = json.dumps(d, indent=indent)
        return string
    def make_dict(self,indent=4):
        type_of_class = self.__class__.__name__
        d = {"type": type_of_class, "dict": {}}
        for k, v in self.__dict__.items():
            if isinstance(v, Jsonable):
                d["dict"][k]= v.make_dict()
            elif isinstance(v, Iterable) and not isinstance(v, str):
                d["dict"][k] = []
                for elem in v:
                    if elem is Jsonable:
                        d["dict"][k].append(elem.make_dict())
                    else:
                        d["dict"][k].append(v)
            else:
                d["dict"][k] = v
        return d

    @classmethod
    def from_json(cls, json_string):
        a = cls()
        d = json.loads(json_string)
        for k, v in d["dict"].items():
            if isinstance(v, dict):
                from_json(globals()[v["type"]],v["dict"])
            setattr(a, k, v)
        return a


class Name(Jsonable):
    def __init__(self,string):
        self.name = string
    def __str__(self):
        return self.name
class Panda(Jsonable, Xmlable):

    def __eq__(self, other):
        return self.name == other.name and self.years == other.years and self.age == other.age

    # def __str__(self):
    #     return "name : " + self.name + " years: " + str(self.years) + " age: " + str(self.age)

    # def __repr__(self):
    #     return +self.__str__

    def __init__(self, name="Empty", years=0, age=0):
        self.name = Name(name)
        self.years = years
        self.age = age
def main():
    p = Panda(name="Ivo", years=15, age=10)
    # a = Panda.from_xml(p.to_xml())
    print(p.to_Json_string())
    # print(Jsonable.from_json(json.loads(p.to_Json_string())))
    # print(p)
    # assert a == p

    # assert q==p


if __name__ == '__main__':
    main()
