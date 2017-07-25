import time
def calc_time(func):
    def calc(*args):
        start_time = get_current_timestamp()
        ret = func(*args)
        end_time = get_current_timestamp()
        print end_time-start_time
        return ret
    return calc
@calc_time
def fac(n):
    if n<2: return 1
    return n * fac(n-1)
get_current_timestamp = lambda : int(round(time.time()*1000))

#fac(5)

def login(act):
    def _login():
        print "Login first"
        act()
    return _login
@login
def access_private_resource():
    print "Then got resource"

access_private_resource()