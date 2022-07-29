from bs4 import BeautifulSoup
import requests

from get_all_tags import get_html_from_url

def get_all_tags(url, id_):
    html_parsed = get_html_from_url(url)
    return html_parsed.find(id=id_)

url = 'https://www.python.org/'
print(f'aqui:{get_all_tags("site-map-link", url)}')