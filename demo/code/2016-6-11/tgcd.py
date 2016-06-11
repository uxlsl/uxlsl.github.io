
import random
from time import time
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor


def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


numbers = [(random.randint(100000, 2000000),
            random.randint(100000, 2000000))
            for _ in range(500)]

start = time()
pool = ProcessPoolExecutor(max_workers=4)
results = list(pool.map(gcd, numbers))
end = time()
print('process take %.3f seconds' % ( end - start))


start = time()
pool = ThreadPoolExecutor(max_workers=4)
results = list(pool.map(gcd, numbers))
end = time()
print('thread take %.3f seconds' % ( end - start))

start = time()
results = list(map(gcd, numbers))
end = time()
print('signal thread take %.3f seconds' % ( end - start))
