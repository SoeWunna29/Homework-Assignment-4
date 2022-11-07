def fltn(_2d_list):
    flat_list = []
    for element in _2d_list:
        if type(element) is list:
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list


x = [[1, 2, 3]]
print(fltn(x))
x = [1, [2, 3], 4]
print(fltn(x))
x = [[1, [1, 1]], 1, [1, 1]]
print(fltn(x))
