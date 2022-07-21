
def remove_duplicates(lista):
    new_list = list(set(lista))
    return new_list

lista = [0,0,1,1,2,2,3,3,4,4,4]
print(len(remove_duplicates(lista)))

