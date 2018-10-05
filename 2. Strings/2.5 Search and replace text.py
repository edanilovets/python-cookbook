import re

# for simple patterns
text_0 = "yeah, but no, but yeah, but no, but yeah"
new_text = text_0.replace("yeah", "yes")
print(new_text)

# for more complex patterns
text_1 = "Today is 11/27/2012. PyCon starts 3/13/2013"
new_text_1 = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text_1)
print(new_text_1)

# try
text_2 = "Showing 1 to 15 of 19 (2 Pages)"
text_inside = re.compile("\((.*)\)").search(text_2).group(1)
words = re.split(r'(?:\s)\s*', text_inside)
print(text_inside)
print(words)
