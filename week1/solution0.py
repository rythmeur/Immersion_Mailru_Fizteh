import sys
'''
Вы должны создать Python модуль solution.py и загрузить его на платформу – этот файл мы запустим с аргументом командной строки – строкой, состоящей из цифр

В списке sys.argv будут лежать аргументы командной строки, sys.argv[0] - имя запущенного файла, sys.argv[1] - строка, сумму цифр которой необходимо посчитать и вывести на экран

import sys


print(sum([int(x) for x in sys.argv[1]]))

'''
digit_string = sys.argv[1]
#print (sys.argv)
#print (digit_string)
counter=0
for char in digit_string:
    digit=int(char)
    counter+=digit
print (counter)

