def f(suits, numbers):
    suit_num = []
    if len(suits) == 0 or len(numbers) == 0:
        return suit_num
    else:
        for i in range(len(suits)):
            for j in range(len(numbers)):
                suit_num.append([suits[i], numbers[j]])
        return suit_num


print(f(['S', 'C'], [1, 2, 3]))
print(f(['S', 'C'], [3, 2, 1]))
print(f([], [3, 2, 1]))
print(f(['S', 'C'], []))
