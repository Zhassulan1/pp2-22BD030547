import re

pattern = r'[a-z]_[a-z]'
text = r'aaaaa_aaaa_aaaaa_ dddd_aa aaaa'
x = re.findall(pattern, text)

print(x)