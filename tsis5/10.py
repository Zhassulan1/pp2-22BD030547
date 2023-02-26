import re

pattern = r'[a-z]*[\s]*[A-Z][a-z]*[\s]*[a-z]*[\s]*'
text = r'SomeWords inSome CamelCase buT Not snakeCase'

result =  re.findall(pattern, text)

string = ''
for i in result:
    if i[-1] != ' ' and i != result[-1]:
        i += '_'
    string += i

#print(result)
print(string)