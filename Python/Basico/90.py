# TODO: Slice de lista. Iniciar a lista com elementos repetidos

def replace_string(string, char, n):
    new = ""
    for counter in range (len(string)-n):
        new += char
    new += string[-5:]
    return new

print(replace_string("kdi39323swe", "*", 5))
print(replace_string("12345abcdef", "*", 5))
print(replace_string("12345", "*", 5))