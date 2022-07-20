

user_input = (input('Digite uma sequência de números separados por vírtula: ')).replace(" ", "")


list = user_input.split(',')
tuple = tuple(list)

print(f'List: {list}')
print(f'Tuple: {tuple}')