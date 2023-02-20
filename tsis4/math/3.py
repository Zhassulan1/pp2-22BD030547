import math

n = int(input("Input number of sides: "))
a = int(input("Input the length of a side: "))

x = a**2 * n / (4 * math.tan(math.pi/n))
print(int(x))