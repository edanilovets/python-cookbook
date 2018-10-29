from fnmatch import fnmatch, fnmatchcase

fnmatch('foo.txt', '*.txt')
fnmatch('Dat45.csv', 'Dat[0. Other-9]*')
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
matches = [name for name in names if fnmatch(name, 'Dat*.csv')]
print(matches)

addresses = ['43 JONES ST', '44 JONES AV', '33 CAROLINE ST']
m1 = [_ for _ in addresses if fnmatchcase(_, '* ST')]
print(m1)
