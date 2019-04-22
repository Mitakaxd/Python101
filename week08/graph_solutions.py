from collections import Iterable
def deep_find(data, key):
    if key in data.keys():
        return data[key]
    value = None
    for k, v in data.items():
        if isinstance(data[k], Iterable):
            value = deep_find(data[k], key)
            if value != None:
                return value
    return None

# print(deep_find({1:2,3:4,4:5,5:{8:9,9:10, 10:{11:12}}},11))


def deep_find_all(data,key, lst=[]):
    if key in data.keys():
        lst.append(data[key])
    for k,v in data.items():
        if isinstance(v,Iterable):
            deep_find_all(v,key,lst)
    return lst
    
# print(deep_find_all({1:2,3:4,4:5,5:{1:9,9:10, 10:{1:12}}},1))

def deep_update(data,key,value):
    if key in data.keys():
        data[key]=value
    for k,v in data.items():
        if isinstance(v,Iterable):
            deep_update(v,key,value)
    return data
    
# print(deep_update({1:2,3:4,4:5,5:{1:9,9:10, 10:{1:12}}},1,5))

def deep_apply(func,data):
    for k,v in data.items():
        data[func(k)] = data.pop(k)
        if isinstance(v,dict):
            deep_apply(func,v)
    return data

def schema_validator(schema: list, data: dict):
    if len(schema) != len(data):
        return False
    for item in schema:
        if not isinstance(item, list):
            if item not in data:
                return False
        else:
            if item[0] not in data:
                return False
            return schema_validator(item[1], data[item[0]])
    return True
schema = [
    'key1',
    'key2',
    [
        'key3',
        ['inner_key1', 'inner_key2']
    ]
]
data = {
    'key1': 'val1',
    'key2': 'val2',
    'key3': {
        'inner_key1': 'val1',
        'inner_key2': 'val2'
    },
    'key4': 'not expected'
}



# print(schema_validator(schema,data))

