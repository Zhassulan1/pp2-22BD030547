import re

pattern = r'[a][b]*'
text = r'aaaaabbbbbbbsdfghsbbsssabbb abbbbb'

x = re.findall(pattern, text)

print(x)