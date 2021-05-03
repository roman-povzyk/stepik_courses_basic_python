lst = [1, 2, 3, 4, 5, 6]


def modify_list(a):
    number = range(len(a))
    for i in number:
        if a[i] % 2 == 0:
            a.clear()
    return a


print(modify_list(lst))
