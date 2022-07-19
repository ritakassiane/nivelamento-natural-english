from random import randint
list = []

def verify(list, value):
    return value in list

for i in range (0,10):
    list.append(randint(0,50))
    print(list)

value = int(input('Digite um número inteiro pra verificar se ele está na lista: '))

print(verify(list, value))
print(list)
