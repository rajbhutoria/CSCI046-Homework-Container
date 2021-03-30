def range(a, b=None, c=None):
    '''
    Built-in python range() function replicated using generators.
    '''
    s = 1
    if c is not None:
        s = c
    
    if b is None:
        x = 0
        yield 0
        while a > s:
            a -= s
            x += s
            yield x
    else:
        x = a
        yield a
        while (b - a) > s:
            b -= s
            x += s
            yield x
