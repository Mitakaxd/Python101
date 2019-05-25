class BaseModelMetaclass(object):
    """docstring for BaseModelMetaclass"""
    def __init__(self, arg):
        super(BaseModelMetaclass, self).__init__()
        self.arg = arg

class Column(object):
    """docstring for Column"""
    def __init__(self, name):
        self.name=name
    def get_constraints(self):
        return ' '.join(self.constraints)
    def as_sql(self):
        #'id Integer PRIMARY KEY AUTOINCREMENT'
        return f'{self.name} {self.column_type}'
class PrimaryKey(Column):
    column_type = 'INTEGER'
    constraints = ('PRIMARY KEY','AUTOINCREMENT')


class BaseModel(metaclass=BaseModelMetaclass):
    """docstring for BaseModel"""
    def __init__(self, arg):
        super(BaseModel, self).__init__()
        self.arg = arg
        