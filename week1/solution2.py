import sys
'''
На вход ваша программа будет получать количество ступенек.

Ваша цель напечатать на экран лесенку используя символы пробела " " и решетки "#". Например, для входного параметра (количества ступенек) 4 лесенка должна выглядеть следующим образом:

import sys

num_steps = int(sys.argv[1])

for i in range(num_steps):
    print(" " * (num_steps - i - 1), "#" * (i + 1), sep="")

'''
num_steps = int(sys.argv[1])

for step in range(num_steps):
    string= " "*(num_steps-step-1) + "#"*(step+1)
    print (string)



