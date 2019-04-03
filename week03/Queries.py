def readCSV(filename):
    def fix_commas_in_strings(row):
        result = ''
        in_string = False
        for ch in row:
            if ch == '"' and in_string:
                in_string = False
            elif ch == '"':
                in_string = True
            if ch == ',' and in_string:
                result += ' '
            else:
                result += ch
        return result
        
    with open(filename) as f:
        lines = f.readlines()
        categories = []
        dataBase = []
        for category in lines[0].strip().split(','):
            categories.append(category)
        lines.pop()
        for row in lines[1:]:
            row = fix_commas_in_strings(row)
            d = {}
            listrow = row.strip().split(',')
            for idx,category in enumerate(categories):
                d[category] = listrow[idx]
            dataBase.append(d)
        return dataBase




def filter(filename, **kwargs):
    data = readCSV(filename)
    print(data)
    result = []
    for row in data:
        flag = True
    #sortby=kwargs["order_by"]
        for key, value in kwargs.items():
            if "_gt" or "_lt" in key:
                temp = key.split('__')
                additional = temp[-1]
                temp.pop()
                key = '_'.join(temp)
                print(row)
                if additional == "_gt":
                    if int(row[key]) < value:
                        flag = False
                        break
                else:
                    if int(row[key]) > value:
                        flag = False
                        break
            elif "_contains" in key:
                temp = key.split('__')
                temp.pop()
                key = '_'.join(temp)
                if value not in row[key]:
                    flag=False
                    break
            else:
                if row[key] != value:
                    flag = False
                    break
                if flag == True:
                    result.append(row)
                else:
                    flag = True
    return result



if __name__ == "__main__":
    print(filter('example_data.csv', salary__gt=1000, salary__lt=3000))
