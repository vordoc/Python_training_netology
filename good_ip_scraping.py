import requests
import bs4

response = requests.get('https://2ip.ru/')
response.raise_for_status()


text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')
d_clip_button = soup.find(id='d_clip_button')
ip_address = d_clip_button.find('span').text
print(ip_address)

