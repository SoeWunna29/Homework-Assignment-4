def add_many(x, el, lst):
    count = 0
    for element in lst:
        if element == x:
            count += 1
    while count > 0:
        lst.append(el)
        count -= 1


lst = [1, 2, 4, 2, 1]
add_many(2, 5, lst)
print(lst)
