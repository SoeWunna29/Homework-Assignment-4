def sym(l):
    pointer1 = 0
    pointer2 = len(l) - 1
    while pointer1 < pointer2:
        if l[pointer1] != l[pointer2]:
            return False
        pointer1 += 1
        pointer2 -= 1
    return True


print(sym([]))
print(sym([1]))
print(sym([1, 4, 5, 1]))
print(sym([1, 4, 4, 1]))
print(sym(['l', 'o', 'l']))
