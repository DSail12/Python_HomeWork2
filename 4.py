# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.


n = int (input ("Введите значение N: "))
list = []
with open('file.txt') as file:
    x = int(file.readline())
    y = int(file.readline())
for i in range(-n,n+1):
    list.append(i)
print (list[x]*list[y])