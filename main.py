import sys
from thread1 import task
from poolthreads import __main__


def main():
     t1 : task = task(1)
     print(t1)



if (__name__ == "__main__"):
    sys.exit(main())