# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0.56 -> 11

number = input('Введите пожалуйста число ')
number = number.replace('.', '')
size = len (number)
number = number
result = 0
for count in range (size):
    result = result + int (number [count])
print (result)