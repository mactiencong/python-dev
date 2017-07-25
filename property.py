class Matico(object):
    def __init__(self, name):
        self.name=name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if(value==None): raise ValueError("Name not empty")
        self._name = value

class NameDesciptor(object):
    def __init__(self, label=None):
        self.lable = label
    def __get__(self, instance, owner):
        return instance.__dict__.get(self.lable)
    def __set__(self, instance, value):
        if(value==None): raise ValueError("Name not empty")
        instance.__dict__[self.lable] = value

class CongMT(object):
    name = NameDesciptor("name")
    def __init__(self, name):
        self.name = name

# matico = Matico("congmt")
# print matico.name

congmt = CongMT("mactiencong")
print congmt.name