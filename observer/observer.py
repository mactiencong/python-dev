from abc import ABCMeta, abstractmethod

class Observer(object):
    @abstractmethod
    def update(self, *args, **kwargs):
        pass