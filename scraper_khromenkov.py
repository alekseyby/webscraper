import requests, time
from bs4 import BeautifulSoup
import re

TIMEOUT = 3
url = 'https://www.amazon.co.uk/gp/offer-listing/B07SXMZLP9/ref=dp_olp_all_mbc?ie=UTF8&condition=all'
page_urls = ''
all_links = []
sellers = []

def data_scraper(url):
    print('Parsing ' + url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    try:
        next_page = soup.find('li', class_="a-last").find('a')['href']
        productLinks = soup.find_all('a', href=True)
        for link in productLinks:
            link = str(link)
            all_links.append(link.encode('utf8'))

        next_page_link = 'https://www.amazon.co.uk' + str(next_page)
        print('Next page is ' + next_page_link)
        return next_page_link
    except TypeError:
        return

for link in url:
    if url == None:
        break
    else:
        url = (data_scraper(url))
        time.sleep(TIMEOUT)

for seller in all_links:
    seller = (seller.decode("utf-8").encode('cp850','replace').decode('cp850'))
    data = re.findall(r'seller\=[0-9A-Z]{14}', seller)
    if data:
        x = data[0]
        sellers.append(x)


print(sellers)
a = set(sellers)
print(a)