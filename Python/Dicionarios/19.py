from collections import Counter

def concatenate_sum_values(dict1, dict2):
    return dict(Counter(dict1) + Counter(dict2))

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

print(concatenate_sum_values(d1,d2))