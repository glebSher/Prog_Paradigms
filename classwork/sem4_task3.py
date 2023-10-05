# Реализовать с использованием функциональной парадигмы процедуру для поиска дубликатов.
# На вход подается массив, где могут присутствовать дубликаты (а могут и не присутствовать).
# При применении к массиву, дубликаты должны быть выведены на экран в виде списка.

def find_duplicates(numbers):
    uniqe_nambers = set()
    return list(filter(lambda x: x in uniqe_nambers or
                                 uniqe_nambers.add(x), numbers))


numbers = [1, 2, 3, 4, 5, 8, 5, 6, 4, 2, 9, 7]
duplicates = find_duplicates(numbers)

print(duplicates)
