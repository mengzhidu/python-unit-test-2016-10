#!/Users/xinguimeng/.pyenv/shims/python

def mengzhidu(n):
    """
    自定义函数，如果传入k，则返回k*(k-1)
    >>> mengzhidu(6)
    22
    >>> mengzhidu(7)
    42
    """
    print(n*(n-1))


def mzd(n):
    """
    自定义函数，如果传入k，则返回k*(k+1)
    >>> mzd(6)
    42
    >>> mzd(5)
    30
    """
    print(n*(n+1))

if __name__ == "__main__":
    import doctest
    doctest.testmod()


