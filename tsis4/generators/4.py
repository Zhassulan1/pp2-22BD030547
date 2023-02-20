def Generator(m,n):
    x = []
    for i in range(m,n+1):
        yield i*i



m = int(input())
n=int(input())

for i in Generator(m,n):
    print(i)
