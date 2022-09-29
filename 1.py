# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

a = input('введите  число')
a = a.replace('.', '')
print(a)
list_str=list(a)
print (list_str)
list_numbers=list(map(int,list_str))
print (list_numbers)
s=sum(list_numbers)
print(s)
#print (a)
#if a==float:
    #a=[int(ele) for ele in str(a) if a.isdigit()]
#else:
    #print(a)
    #a = [int (x) for x in a]
    #a = [int (a) for x in a]
    #a=list( map(int,a))
#else:
    #print(list(a))

#list.pop[1]
#print(list(a))


#result = [int(item) for item in a]


#def concatenatio(list):
    #res: int=0
    #for i in list:
        #res+=i
        #return res