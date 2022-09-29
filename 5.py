#Реализуйте алгоритм перемешивания списка.

a=int(input('введите число  a'))
#for i in range(a):
    #print(i)
list=list(range(a))
print(list)
import random
random.shuffle(list)
print(list)
