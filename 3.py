# Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
# Пример:
# 1 -> 2.0
# 2 -> 4.25
# 3 -> 6.62037037037037


n = int(input("Введите пожалуйста число n: "))
summa = 0
count = 1
while count <= n:
    x = ((1+1 / count)**count)
    summa +=  x
    count += 1
print(summa)