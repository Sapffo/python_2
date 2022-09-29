#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

a=int(input('введите число N'))
b=int(input('введите число -N'))
#for x in range(-b,a):
    #print (x)
numbers=list(range(-b,a))
print (numbers)
for i in numbers:
    if numbers[i]==0:
        del numbers[i]
else:
    print(numbers)
product=1
for i in numbers:
    product*=i
    print (product)
