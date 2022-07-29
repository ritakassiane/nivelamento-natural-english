
# TODO: buscar uma solução diferente. join
# A função abaixo recebe uma lista e concatena seus itens em uma única string
def join(list):
    result = ""
    for i in list:
        result+=str(i)
    return result

listaTeste = ['Natural', 'English','Institue']
listaTeste2 = [1, 2, 3, 4]

print(join(listaTeste))
print(join(listaTeste2))