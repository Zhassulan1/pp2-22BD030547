import re

pattern = r'a.*b'
text = r'adfghb acvnn b b a'

x = re.findall(pattern, text)

print(x)