import re

text = r'some.text,words space'
modified = re.sub(r'[\s\.,]+', ':', text)
print(modified)