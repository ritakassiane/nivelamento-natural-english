from collections import Counter

def top_items(dict_, n):
    print(Counter(dict_))
    return dict(Counter(dict_).most_common(n))



A = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}

print(top_items(A,3))