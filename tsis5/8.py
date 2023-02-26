import re

pattern = r'[a-z]*[\s]*[a-z]*[A-Z][a-z]*[\s]*[a-z]*'
text = r'SomeText In upperCase Letter ToBeSplitted'

result = re.findall(pattern, text)
print(result)