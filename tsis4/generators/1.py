def generator(n):
    for i in range(0,n+1):
        yield (i*i)

for i in generator(5):
    print(i)