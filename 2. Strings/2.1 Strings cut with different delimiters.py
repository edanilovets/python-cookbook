import re

line = "Hello world, this is my time; to say."
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)
values = fields[::2]
delimiters = fields[1::2]
print(values)
print(delimiters)

fields1 = re.split(r'(?:;|,|\s)\s*', line)
print(fields1)
