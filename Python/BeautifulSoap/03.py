from get_all_tags import get_all_tags


url = 'https://en.wikipedia.org/wiki/Parsing'

print(len(get_all_tags("p", url)))