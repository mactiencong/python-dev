observer_collection = []
def register(observer):
    if observer not in observer_collection:
        observer_collection.append(observer)
def unregister(observer):
    if observer in observer_collection:
        observer_collection.remove(observer)
def noify(*args, **kwargs):
    for observer in observer_collection:
        observer.update(*args, **kwargs)