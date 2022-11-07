def chk_elm(lst, n):
    for element in lst:
        if isinstance(element, list):
            if chk_elm(element, n):
                return True
        elif element == n:
            return True
    return False


a = [[1, [2]], 3, [[4], [5, [6]]]]
print(chk_elm(a, 6))
