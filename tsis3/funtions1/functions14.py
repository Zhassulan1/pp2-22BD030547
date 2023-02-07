def toGrams(num):
    print(num / 28.3495231)

def antiFar(num):
    print((num-32)*5/9)

def toCentimeter(num):
    print(num * 2.54)


print("Enter the number")
print("1)Convert ounces to gramms")
print("2)Convert Farenheit to Celcius")
print("3)Convert inches to centimeters")

mode = int(input())

if mode == 1:
    print("Enter the value")
    value = float(input())
    toGrams(value)
elif mode == 2: 
    print("Enter the value")
    value = float(input())
    antiFar(value)
elif mode == 3:
    print("Enter the value")
    value = float(input())
    toCentimeter(value)
else:
    print("An Error Occured")