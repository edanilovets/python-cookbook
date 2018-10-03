
import re

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
text = "Today is 11/27/2012. PyCon starts 3/12/2013"

# \d+ means match of 1 or more numbers
date_pattern = re.compile(r'\d+/\d+/\d+')
print('Yes') if re.match(r'\d+/\d+/\d+', text1) else print('No')
print("Match: {}".format(date_pattern.match(text1)))
print("Find all: {}".format(date_pattern.findall(text)))

# groups
date_pattern_1 = re.compile(r'(\d+)/(\d+)/(\d+)')
m = date_pattern_1.match('11/27/2012')
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())


print("Find all: {}".format(date_pattern_1.findall(text)))
for month, day, year in date_pattern_1.findall(text):
    print('{}-{}-{}'.format(year, month, day))
