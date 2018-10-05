import re


text = "UPPER PYTHON, lower python, Mixed Python"
matches = re.findall('python', text, flags=re.IGNORECASE)
print(matches)
new_text = re.sub('python', 'snake', text, flags=re.IGNORECASE)
print(new_text)
