import re

pattern = r'ab{2,3}'
text = r'abbb aaaaabbbbbbbsdfghsbbsssabbb  abb abbb abbbbb'

x = re.findall(pattern, text)

print(x)