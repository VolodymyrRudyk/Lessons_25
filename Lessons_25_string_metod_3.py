line = "The knights who say Ni!\n"
print(line.rstrip())
print(line.upper())
print(line.isalpha())
print(line.endswith('Ni!\n'))
print(line.startswith('The'))

print(line)
print(line.find('Ni') != -1)                #пошук через виклик методу чи виразу
print('Ni' in line)
sub = 'Ni!\n'
print(line.endswith(sub))                   #перевірка наявності підстроки в кінці через виклик методу чи зрізу
print(line[-len(sub):] == sub)