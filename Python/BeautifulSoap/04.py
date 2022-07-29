from get_all_tags import get_all_tags

url = 'https://en.wikipedia.org/wiki/Parsing'

def get_paragraph_x(x):
    print(f'O paràgrafo {x} é : {get_all_tags("p", url)[x]}')
    return ""
    

print(get_paragraph_x(0))
