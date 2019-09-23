import timeit
from Assign02.fibonacchi import *

if __name__ == "__main__":

    print("방법")
    print("1 - Recursion")
    print("2 - Array")
    print("3 - Recursive Squaring")
    method = int(input())

    print("테스트할 숫자")
    inp = int(input())
    start = timeit.default_timer()

    if   (method == 1):
        print('*** Method 1 ***')
        for i in range(0, inp + 1):
            if i % 10 == 0:
                print('-' * 80)
            ret = fibonacci_recursive(i)
            result = "%40s" % ("%d %0.10f" % (ret, timeit.default_timer() - start))
            print('f<%2s> = %s' % (i, result))

    elif (method == 2):
        print('*** Method 2 ***')
        for i in range(0, inp + 1):
            if i % 10 == 0:
                print('-' * 80)
            ret = fibonacci_bottomup(i)
            result = "%40s" % ("%d %0.10f" % (ret, timeit.default_timer() - start))
            print('f<%2s> = %s' % (i, result))

    elif (method == 3):
        print('*** Method 3 ***')
        for i in range(0, inp + 1):
            if i % 10 == 0:
                print('-' * 80)
            ret = fibonacci_squaring(i)
            result = "%40s" % ("%d %0.10f" % (ret, timeit.default_timer() - start))
            print('f<%2s> = %s' % (i, result))

