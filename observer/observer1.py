from observer import Observer
from observable import register
class Observer1(Observer):
    def __init__(self):
        register(self)
    def update(self, *args, **kwargs):
        print "Observer1 updated"
        print args
        print kwargs