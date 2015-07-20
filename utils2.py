__author__ = 'Samuel'

def fib(n):
    """Print the Fibonacci series up to n."""
    a = 0
    b = 1
    i = 0
    while i < n:
        a, b, i = b, a + b, i + 1
    return b
