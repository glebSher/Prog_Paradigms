# Написать скрипт принимающий на вход массив с данными о людях и
# число - возраст, а возвращающий число - количество людей старше указанного возраста.

people = [
    {'name': 'Elizaveta', 'age': 26},
    {'name': 'Vasiliy', 'age': 31},
    {'name': 'Sergey', 'age': 35},
    {'name': 'Ivan', 'age': 40}
]


def filter_by_age(people: list, min_age: int) -> list:
    return list(filter(lambda pers: min_age <= pers['age'], people))


age = 30
filtered_people = filter_by_age(people, age)

print(filtered_people)
print(len(filtered_people))
