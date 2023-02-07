from itertools import permutations 

str = input()
perm = permutations(str)
for i in list(perm):
    for j in i:
        print(j, end = '')
    print("")