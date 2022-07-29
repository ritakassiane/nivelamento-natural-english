# def concatenate_dict(*dicts):
#     dict_result = {}
#     for dict in dicts:
#         dict_result.update(dict)
#     return dict_result

def concatenate_dict(*dicts):
    dict_result = {k: v for dict in (dicts) for k,v in dict.items()}
    return dict_result

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

print(concatenate_dict(dic1, dic2, dic3))