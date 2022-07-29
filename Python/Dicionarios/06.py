# def dict_n_elements_square(n):
#     dict = {}
#     for element in range (1,n+1):
#         dict[element]=element**2
#     return dict


def dict_n_elements_square(n):
    dict = {elemento: elemento**2 for elemento in range(1,n+1)}
    return dict


print(dict_n_elements_square((15)))

