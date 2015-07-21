__author__ = 'Samuel'

import sys
import subprocess
subprocess.call([sys.executable, 'setup.py', 'build_ext', '--inplace'])
import utils
import utils2
import time

n = 10000000

print("Cython with enhancements  ", end=' ')
t0 = time.time()
print(utils.logistic_map(n), end=' ')
print(time.time() - t0)

print("Cython no enhancements    ", end=' ')
t0 = time.time()
print(utils.logistic_map2(n), end=' ')
print(time.time() - t0)

print("Python                    ", end=' ')
t0 = time.time()
print(utils2.logistic_map(n), end=' ')
print(time.time() - t0)
