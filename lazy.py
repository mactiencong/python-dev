def lazy(property_func):
    attr = "attr_" + property_func.__name__
    @property
    def data(self):
        if not hasattr(self, attr):
            setattr(self, attr, property_func(self))
        return getattr(self, attr)
    @data.setter
    def data(self, value):
        setattr(self, attr, value)

    return data

class Person(object):
    @lazy
    def name(self):
        print "get name"
        return "matico"

matico = Person()
print matico.name
print matico.name
print matico.name

matico.name = "congmt"
print matico.name