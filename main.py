__author__ = 'Samuel'

import subprocess
subprocess.call(['C:/Anaconda3/python.exe', 'setup.py', 'build_ext', '--inplace'])
import utils

print(utils.fib(10))
