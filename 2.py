#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

a=int(input('введите число N'))

#for i in range(a):
    #print (i)
numbers=list(range(1,a+1))
print (numbers)
product=1
for i in numbers:
    product*=i
    print (product)
           
