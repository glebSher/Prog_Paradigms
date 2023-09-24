def searchImeprative(number, array):
    for i in range(len(array)):
        if array[i] == number:
            return True
    return False

print(searchImeprative(5, [1,2,3,4]))