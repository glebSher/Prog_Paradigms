# ИМПЕРАТИВНЫЙ ВАРИАНТ:
# На вход подается: список целых чисел arr
# ● Задача
# Реализовать императивную функцию, которая возвращает три числа:
# ○ Долю позитивных чисел
# ○ Долю нулей
# ○ Долю отрицательных чисел

def Imperative(array):
    positive, negative, zero = 0,0,0
    for i in array:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1
    positive = positive / len(array)
    negative = negative / len(array)
    zero = zero / len(array)
    return positive, negative, zero

print(Imperative([1,5,-6,0,4,-7,0,6,-8, 12]))
