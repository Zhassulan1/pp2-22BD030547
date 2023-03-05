string = "Some Word"
upper, lower = 0, 0

for i in string:
    if 65 <= ord(i) <= 90:
        upper += 1
    if 97 <= ord(i) <= 122:
        lower += 1


print(f"{upper} upper case letters")
print(f"{lower} lower case letters")