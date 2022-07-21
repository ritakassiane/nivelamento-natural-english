
 

def match_key_values(dict1, dict2):
    for (key, value) in set(dict1.items()) & set(dict2.items()):
        print(f'{key}:{value} está presente em ambos dicionários')

match_key_values({'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2})

