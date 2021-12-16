import requests
import bs4

HEADERS = {
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cookie': '_ym_d=1629641837; _ym_uid=1629641837125718007; _ga=GA1.2.546607213.1629641837; fl=ru; hl=ru; __gads=ID=9ad4ffbc5e76dca8:T=1629641839:S=ALNI_MbuBu9JtN1hiGHH3bPX1d6D2Gn83A; feature_streaming_comments=true; cto_bundle=ELMIs19KMVFBMnRUSVhJYzZYWkZNVmxzeW5ydmR2RlIwWHpHdVdrODlXYWNmUDZtb3cwYXk2c242S0tFRW03bm4yNTBjcEk3dzZWWWpuZU11NGolMkZQenYlMkZkMzdXZFFNdGNrcTh4S0pGVTFqVzBrTFB0SVFyY09yV0cySjdINEo2QU9lcGthbWFrN0FLMWVKRkVQd1J1d2RzS3ZnJTNEJTNE; _gid=GA1.2.597561276.1639572658; _ym_isad=2; habr_web_home=ARTICLES_LIST_ALL; _gat=1',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
}

MY_TAGS = {'Конференции', 'Управление персоналом'}

response = requests.get('https://habr.com/ru/news/', headers=HEADERS)
response.raise_for_status()

text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')
# article = soup.find('article')
articles = soup.find_all('article')
for article in articles:
    hubs = article.find_all('a', class_='tm-article-snippet__hubs-item-link')
    # hubs = [hub.find('span').text for hub in hubs]
    hubs = set([hub.find('span').text for hub in hubs])
    title = article.find('a', class_='tm-article-snippet__title-link')
    span_title = title.find('span').text
    if MY_TAGS & hubs:
        href = title['href']
        url = 'https://habr.com' + href
        print(span_title, url)
        print(hubs)
        print('-------------')
# print(len(articles))

