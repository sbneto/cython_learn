__author__ = 'Samuel'

import subprocess
subprocess.call(['C:/Anaconda3/python.exe', 'setup.py', 'build_ext', '--inplace'])
import utils
import utils2
import time

n = 10000000

print("Cython with enhancements\t", end=' ')
t0 = time.time()
print(utils.logistic_map(n), end=' ')
print(time.time() - t0)

print("Cython no enhancements\t\t", end=' ')
t0 = time.time()
print(utils.logistic_map2(n), end=' ')
print(time.time() - t0)

print("Python\t\t\t\t\t\t", end=' ')
t0 = time.time()
print(utils2.logistic_map(n), end=' ')
print(time.time() - t0)
