from observer import Observer
from observable import register
class Observer2(Observer):
    def __init__(self):
        register(self)
    def update(self, *args, **kwargs):
        print "Observer2 updated"
        print args
        print kwargs