some = [1, 5, 6, 9, 65562, 9, 65, 6, 5, 3, 2, 7, 11, 13, 8]
filtered = []


def filter(num):
    i = 2
    while i <= num**0.5:
        if num % i == 0:
            return False
        i += 1
    return True

for num in some:
    if filter(num) == True:
        filtered.append(num)

print(filtered)