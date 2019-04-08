from contextlib import contextmanager
import datetime
from time import sleep
@contextmanager
def performance(file_name):
    with open(file_name,'a') as f:
        time_now = datetime.datetime.now()
        yield
        time_elapsed = (datetime.datetime.now() - time_now)
        f.write(str(datetime.datetime.now()) + " Execution time: " + str(time_elapsed) + '\n')

# def myTestfunc():
#     with performance('log.txt'):
#         sleep(1)

# myTestfunc()
# myTestfunc()
@contextmanager
def assertRaises(exception,msg=None):
    try:
        yield
    except exception:
        pass
    else:
        raise Exception(msg)


def testing_assert_raises():
    with assertRaises(IndexError,"I didnt hit anything"):
        lst = []
        print('a' + 5)


testing_assert_raises()
