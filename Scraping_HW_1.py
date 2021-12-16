import requests
import bs4

HEADERS = {
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cookie': '_ym_d=1629641837; _ym_uid=1629641837125718007; _ga=GA1.2.546607213.1629641837; fl=ru; hl=ru; '
              '__gads=ID=9ad4ffbc5e76dca8:T=1629641839:S=ALNI_MbuBu9JtN1hiGHH3bPX1d6D2Gn83A; '
              'feature_streaming_comments=true; cto_bundle=ELMIs19KMVFBMnRUSVhJYzZYWkZNVmxzeW5ydmR2RlIwWHpHdVd'
              'rODlXYWNmUDZtb3cwYXk2c242S0tFRW03bm4yNTBjcEk3dzZWWWpuZU11NGolMkZQenYlMkZkMzdXZFFNdGNrcTh4S0pGVT'
              'FqVzBrTFB0SVFyY09yV0cySjdINEo2QU9lcGthbWFrN0FLMWVKRkVQd1J1d2RzS3ZnJTNEJTNE; _gid=GA1.2.597561276.'
              '1639572658; _ym_isad=2; habr_web_home=ARTICLES_LIST_ALL',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
}

KEYWORDS = {'Конференции', 'Управление персоналом', 'Робототехника', 'Искусственный интеллект'}

response = requests.get('https://habr.com/ru/all/', headers=HEADERS)
response.raise_for_status()

text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')

for article in articles:
    title_common = article.find_all('a', class_='tm-article-snippet__title-link')
    categories_common = article.find_all('a', class_='tm-article-snippet__hubs-item-link')
    main_common = article.find_all('p')
    title_link = article.find('a', class_='tm-article-snippet__title-link')
    time = article.find('time')

    title_text = set([title_text.find('span').text for title_text in title_common])
    categories_text = set([categories_text.find('span').text for categories_text in categories_common])
    main_text = set([main_text.text for main_text in main_common])

    if KEYWORDS & title_text or KEYWORDS & categories_text or KEYWORDS & main_text:
        href = title_link['href']
        url = 'https://habr.com' + href
        print(time['title'])
        print(title_text)
        print(url)
        print('-------------')
