def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    n = max(a, b) + 1
    while n % max(a, b) != 0 or n % min(a, b) != 0:
        n = n + 1
    return n


def unique_digits(n):
    """Return the number of unique digits in positive integer n

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    k, i = 0, 0
    while k < 10:
        if has_digit(n, k):
            i = i + 1
        k = k + 1
    return i

def has_digit(n, k):
    while n // 10 > 0:
        n, m = n // 10, n % 10
        if m == k:
            return True
    if n == k:
        return True
