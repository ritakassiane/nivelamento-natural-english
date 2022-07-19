
#TODO: Limpar espaços
user_input = input('Digite uma sequência de números separados por vírtula: ')

list = user_input.split(',')
tuple = tuple(list)

print(f'List: {list}')
print(f'Tuple: {tuple}')