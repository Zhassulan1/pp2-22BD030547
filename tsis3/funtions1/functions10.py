def uniquer(list):
    new = []
    for i in range(len(list)):
        if len(new) == 0 or list[i] not in new:
            new.append(list[i])
    return new

ls = [1, 2, 3, 5, 6, 7, 8, 9, 11, 5, 6, 1, 1, 2, 3, 3, 3, 3, 4, 9]

print(uniquer(ls))