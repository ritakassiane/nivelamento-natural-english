
def group_dict(list_):
    result = {}
    for key, value in list_:
        result.setdefault(key, []).append(value)
    return result
    
print(group_dict([('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1),('yellow', 1)]))