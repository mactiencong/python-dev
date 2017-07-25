# with open("lazy.py", "r") as filehandler:
#     lines = filehandler.readlines()
#     for line in lines:
#         print line

from contextlib import contextmanager
@contextmanager
def read_file():
    print "reading ..."
    yield
    print "close file"

# with read_file():
#     print "done"

class File:
    filehandler = None
    def __init__(self, filename, mode):
        print filename, mode
        self.filehandler = open(filename, mode)
    def __enter__(self, *args, **fwargs):
        print "__enter__"
        print args
        print fwargs
        print "__end enter__"
        return self.filehandler
    def __exit__(self, type, value, traceback):
        print "__exit__"
        print type
        print traceback
        print "__end exit__"
        self.filehandler.close()
        return True
with File("lazy.py", "r") as filehandler:
    filehandler.abc()
    
