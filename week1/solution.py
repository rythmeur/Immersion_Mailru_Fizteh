import sys
'''
На вход программе мы подадим коэффициенты a, b и c - ваша цель напечатать 2 корня квадратного уравнения (каждый с новой строки).

Корни должны быть приведены к целочисленному виду перед выводом на экран, порядок вывода корней произвольный. Успехов в решении!

import sys
import math

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

d = b * b - 4 * a * c

x1 = (-b + math.sqrt(d)) / (2 * a)
x2 = (-b - math.sqrt(d)) / (2 * a)

print(int(x1))
print(int(x2))


'''
import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
#print (sys.argv)

x1=(-b +((b**2)-(4*a*c))**(1/2))/ (2*a)
x2=(-b -((b**2)-(4*a*c))**(1/2))/ (2*a)
print (int(x1))
print (int(x2))

