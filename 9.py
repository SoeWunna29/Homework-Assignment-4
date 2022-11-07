def sub(a, b):
    return a - b


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def fld(lst, g, m):
    if len(lst) == 0:
        return m
    else:
        m = g(m, lst[0])
        lst.pop(0)
        return fld(lst, g, m)


s = [3, 2, 1]
print(fld(s, sub, 0))
print(fld(s, add, 0))
print(fld(s, mul, 1))
print(fld([], sub, 100))
