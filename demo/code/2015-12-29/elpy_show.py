"elpy show"


def fib(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
        print
        print a
fib(1000)

import requests
