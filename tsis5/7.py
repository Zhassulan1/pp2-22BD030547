import re

def toCamel(tuple):
    word1, word2 = tuple[0], tuple[1]
    word2 = word2.capitalize()
    word1 += word2
    return word1


pattern = r'(?P<first>[A-Za-z][a-z]*)_(?P<second>[a-z]+)'
text = r'Some_words in_some snake_case but_ _not Camel_Case'

results = re.findall(pattern, text)

for i in range(len(results)):
    results[i] = toCamel(results[i])

print(results)