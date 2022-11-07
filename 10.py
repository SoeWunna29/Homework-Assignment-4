def crte_2d_arr(rows, columns):
    ar_2d = [[0] * columns] * rows
    for i in range(rows):
        for j in range(columns):
            ar_2d[i][j] = "-"
    return ar_2d


print(crte_2d_arr(3, 5))
