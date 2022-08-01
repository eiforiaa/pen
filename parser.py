from bs4 import BeautifulSoup
import requests
# from aiogram import Bot, Dispatcher, types
# from aiogram.utils import executor
#url = 'https://www.sberbank.ru/ru/person/credits/homenew'
URL = 'https://yandex.ru'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15', 'Accept': '*/*'}
#headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
#headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.134 YaBrowser/22.7.0.1925 Yowser/2.5 Safari/537.36', 'accept': '*/*'}

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('a', class_="news__item-inner")
    #'kitt-col kitt-col_xs_12 kitt-col_md_6 product-catalog__card-block')
    print(items)

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        #print(html.text)
        get_content(html.text)
    else:
        print('Error')

parse()


# request = requests.get(url)
#
# teme = soup.find_all('td', class_='paragraph')
# print(soup)
# for temes in teme:
#     temes = temes.find('a', {'class':'kitt-text kitt-text_size_m product-catalog__description product-catalog__description_mobile'})
#     if temes is not None and 'Ставка' in str(temes):
#         sublink = temes.get('href')
#         print(str(temes.text) + ' ' + str(sublink))
