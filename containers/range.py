def range(a, b=None, c=None):
    '''
    Built-in python range() function replicated using generators.
    '''

    global n
    if b is not None:
        if b > a:
            n = b
        else:
            n = a
    else:
        n = a

    global s
    if c is not None and c > 1:
        s = c
    else:
        s = 1

    if n == 0:
        return
    if n == 1:
        yield 0
    else:
        x = 0
        while n > s:
            n -= s
            x += s
            yield x
