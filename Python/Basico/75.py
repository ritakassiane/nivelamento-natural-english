
# def remove_value(array, value):
#     while value in array:
#         array.remove(value)
#     return len(array)

# TODO: refazer utilizando funções lambda
def remove_value(array, value):
    array = list(filter((value).__ne__, array)) #.__ne__ verify if value exists in array and return a bool
    return len(array)

print(remove_value([1, 2, 3, 4, 5, 6, 7, 5], 5))
print(remove_value([10,10,10 ,10,10], 20))
print(remove_value([10,10,10,10,10], 10))
print(remove_value([], 1))