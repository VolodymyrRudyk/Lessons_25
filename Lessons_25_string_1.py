S = 'spam'
#S = [0] = 'x'                                  #виникає помилка, бо строки незмінні
S = S + 'SPAM!'                                 #щоб змінити строку, необідно створити нову строку
print(S)
S = S[:4] + 'Burger' + S[-1]
print(S)

S = 'splot'
S = S.replace('pl', 'pamal')
print(S)

print('That is %d %s bird!' % (1, 'dead'))      #вираз форматування
print('That is {0} {1} bird!'.format(1, 'dead'))#метод форматування