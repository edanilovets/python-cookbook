import re

str_pat = re.compile(r'\"(.*)\"')

text1 = 'Computers say "no."'
print(str_pat.findall(text1))
text2 = '"yes" Computers say "no."'
print(str_pat.findall(text2))

str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text2))