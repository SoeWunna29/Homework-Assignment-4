def mrg(ls1, ls2):
    merged_lst = []
    one = 0
    two = 0

    while one < len(ls1) and two < len(ls2):
        if ls1[one] < ls2[two]:
            merged_lst.append(ls1[one])
            one += 1
        else:
            merged_lst.append(ls2[two])
            two += 1

    merged_lst = merged_lst + ls1[one:] + ls2[two:]
    return merged_lst


print(mrg([1, 3, 5], [2, 4, 6]))
print(mrg([], [2, 4, 6]))
print(mrg([1, 2, 3], []))
print(mrg([5, 7], [2, 4, 6]))
