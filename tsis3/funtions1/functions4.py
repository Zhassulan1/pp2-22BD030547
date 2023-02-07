def filter(num):
    i = 2
    while i <= num**0.5:
        if num % i == 0:
            return False
        i += 1
    return True


def filter_prime(some_list):
    filtered = []
    for num in some_list:
        if filter(num) == True:
            filtered.append(num)
    return filtered



list1 = [1, 2, 3, 4, 5, 9, 15, 11, 13]
print(filter_prime(list1))