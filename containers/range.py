def range(a, b=None, c=None):
    '''
    Built-in python range() function replicated using generators.
    '''
    if b is None:
        b = a
        a = 0

    s = 1
    if c is not None:
        s = c

    case1 = False
    case2 = False

    if a > b:
        case1 = True
    else:
        case2 = True

    x = a
    if (b - a) / s < 0:
        return []
    if case1 is True:
        while x > b:
            yield x
            x += s
    if case2 is True:
        while x < b:
            yield x
            x += s
