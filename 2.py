def rm_all(elem, lst):
    answer = [i for i in lst if i != elem]
    return answer


x = [3, 1, 2, 1, 5, 1, 1, 7]
print(rm_all(1, x))
