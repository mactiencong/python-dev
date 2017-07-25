import threading
import math

def is_prime(number):
    number_sqrt =  int(math.sqrt(number))
    for i in xrange(2, number_sqrt+1):
        if number % i ==0:
            return False
    return True

class Counter(threading.Thread):
    def __init__(self, numbers, primes, numbers_lock, primes_lock, thread_number):
        threading.Thread.__init__(self)
        self.__numbers = numbers
        self.__primes = primes
        self.__numbers_lock = numbers_lock
        self.__primes_lock = primes_lock
        self.__thread_number = thread_number
    def run(self):
        print "Start running thread " + self.__thread_number
        while True:
            with self.__numbers_lock:
                try:
                    print self.__thread_number + "locked"
                    number = next(self.__numbers)
                except Exception:
                    print self.__thread_number + " stoped!"
                    return
            print self.__thread_number + " check prime " + str(number)
            if is_prime(number):
                print str(number) + " is prime"
                with self.__primes_lock:
                    self.__primes.append(number)
                    print self.__primes
        print self.__thread_number + " stoped"
#main
numbers = (number for number in range(2, 101))
numbers_lock = threading.Lock()
primes = []
primes_lock = threading.Lock()
number_parallel = 5
threads = []
for i in range(number_parallel):
    thread = Counter(numbers, primes, numbers_lock, primes_lock, str(i))
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()
print "done"
print primes