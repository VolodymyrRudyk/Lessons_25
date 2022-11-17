S = 'spam'
result = S.find('pa')                       #виклик методу find для пошуку 'pa' в строці S
print(result)

S = 'spammy'
S = S[:3] + 'xx' + S[5:]                    #нарізаємо сегменти з S
print(S)

S = 'spammy'
S = S.replace('mm', 'xx')                   #замінити всі mm на xx в S
print(S)

print('aa$bb$cc$dd'.replace('$', 'SPAM'))

S = 'xxxxSPAMxxxxSPAMxxxx'
where = S.find('SPAM')                      #пошук позиції
print(where)                                #знайшлась по зміщенню 4

S = S[:where] + 'EGGS' + S[(where+4):]
print(S)

S = 'xxxxSPAMxxxxSPAMxxxx'
print(S.replace('SPAM', 'EGGS'))            #замінити все
print(S.replace('SPAM', 'EGGS', 1))         #змінити одну

S = 'spammy'
L = list(S)
print(L)
L[3] = 'x'                                  #працює для списків але не для строк
L[4] = 'x'
print(L)
S = ''.join(L)
print(S)

print('SPAM'.join(['eggs', 'sousage', 'ham', 'toast']))
