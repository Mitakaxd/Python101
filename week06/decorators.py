import datetime
import time
import unittest

def accepts(*argtypes):
    def accepter(func):
        def decorated(*args):
            for idx,arg in enumerate(args):
                if type(arg) != argtypes[idx]:
                    raise TypeError("Argument {} of {} is not {}".format(idx+1,func.__name__,argtypes[idx]))
            else:
                return func(args)
        return decorated
    return accepter

def log(file_name):
    def accepter(func):
        def decorated():
            with open(file_name,'a') as log:
                log.write(func.__name__ + " was called at "+ str(datetime.datetime.now())+'\n')
            return func()
        return decorated
    return accepter


@accepts(int,str)
def say_hello(name):
    return "Hello, I am {}".format(name)

def encrypt(key):
    def accepter(func):
        def decorated():
            return (''.join([chr(ord(ch) + key) for ch in func()])).replace(chr(ord(' ')+key),' ')
        return decorated
    return accepter

@log('log.txt')
def get_low():
    return "Get get get low"

def performance(file_name):
    def accepter(func):
        def decorated():
            time_now = datetime.datetime.now()
            func()
            time_taken_for_func = datetime.datetime.now() - time_now
            with open(file_name,'a') as log:
                log.write(func.__name__ + " was called and took " + str(round(time_taken_for_func.total_seconds(),2)) + " to complete\n")
            return
        return decorated
    return accepter

@performance('log2.txt')
def something_heavy():
    time.sleep(2)
    return "I am done!"

something_heavy()

