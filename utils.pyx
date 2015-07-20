
cpdef long fib(long n):
    """Print the Fibonacci series up to n."""
    cdef long a = 0
    cdef long b = 1
    cdef long i = 0
    while i < n:
        a, b, i = b, a + b, i + 1
    return b

def fib2(n):
    """Print the Fibonacci series up to n."""
    a = 0
    b = 1
    i = 0
    while i < n:
        a, b, i = b, a + b, i + 1
    return b
