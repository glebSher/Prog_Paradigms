# Десятичное в двоичное
# ● Условие: На вход подается число в десятичной системе счисления
# ● Задача: Написать скрипт в любой парадигме, который возвращает
# полученное число переведенное в двоичную систему счисления.
# Обоснуйте сделанный выбор парадигм.

def decToBin(decNumber):
    binNumber = ''
    while decNumber > 0:
        binNumber = str(decNumber % 2) + binNumber
        decNumber = decNumber // 2
    return binNumber

number = int(input("Введите число n: "))

print(decToBin(number))