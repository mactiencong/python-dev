from observable import unregister, noify
from observer1 import Observer1
from observer2 import Observer2

ob1 = Observer1()
ob2 = Observer2()

noify(data="update di nhe")

unregister(ob1)

noify(data="update lan 2")