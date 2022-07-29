from bs4 import BeautifulSoup
import requests

## Questão 02 ## 


def get_html_from_url(url):
    req = requests.get(url)
    html_parsed = BeautifulSoup(req.content, 'html.parser')

    return html_parsed

def get_all_tags(tag, url):
    html_parsed = get_html_from_url(url)
    return html_parsed.find_all(tag)

url = 'https://en.wikipedia.org/wiki/Parsing'

print(get_all_tags("p", url))