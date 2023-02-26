import re

pattern = r'[A-Z][a-z]+'
text = r"AAAdddd adss Vvvvv vadsA"

x = re.findall(pattern, text)

print(x)