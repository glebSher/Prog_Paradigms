def Declarative(array):
    positive = len(list(filter(lambda x: x > 0, array)))
    negative = len(list(filter(lambda x: x < 0, array)))
    zero = len(list(filter(lambda x: x == 0, array)))
    count = [positive, negative, zero]
    return list(map(lambda x: x/len(array), count))

print(Declarative([1,3,5,-7,-6,0,4,-8,0,-18]))