from get_all_tags import get_all_tags

def get_all_hrefs_in_li(li_list):
    links = []
    for li in li_list:
        a = li.find_all('a')
        links.append(a.attrs['href'])
    return links


url = 'https://www.python.org/'

li_list = get_all_tags("li", url)

print(get_all_hrefs_in_li(li_list))