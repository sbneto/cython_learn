__author__ = 'Samuel'

from distutils.core import setup
from Cython.Build import cythonize

setup(name='fib',
      ext_modules=cythonize("*.pyx", language_level=3))
