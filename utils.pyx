
cpdef double fib(double n):
    """Print the Fibonacci series up to n."""
    cdef double a = 0
    cdef double b = 1
    cdef double i = 0
    while i < n:
        a, b, i = b, a + b, i + 1
    return b


cpdef double logistic_map(double n):
    """Print the Fibonacci series up to n."""
    cdef double x = 0.5
    cdef double r = 3.6
    cdef double i = 0
    while i < n:
        x, i = r * x * (1 - x), i + 1
    return x


def fib2(n):
    """Print the Fibonacci series up to n."""
    a = 0
    b = 1
    i = 0
    while i < n:
        a, b, i = b, a + b, i + 1
    return b


def logistic_map2(n):
    """Print the Fibonacci series up to n."""
    x = 0.5
    r = 3.6
    i = 0
    while i < n:
        x, i = r * x * (1 - x), i + 1
    return x