import re

pattern = r'[a-z]*[\s]*[A-Z][a-z]*[\s]*'
text = r'SomeTextInupperCase Letter ToBeSplitted'

result = re.findall(pattern, text)

string = ''

for i in result:
    if i[-1] != ' ':
        i += ' '
    string += i

print(string)