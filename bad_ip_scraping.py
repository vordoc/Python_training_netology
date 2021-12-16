import requests

response = requests.get('https://2ip.ru/')
response.raise_for_status()

text = response.text

# print(text.find('span'))
# print(text.find('d_clip_button'))

d_clip_button_pos = text.find('d_clip_button')
ip_pos = text.find('<span>', d_clip_button_pos)
ip_pos_end = text.find('</span>', d_clip_button_pos)
print(ip_pos)

print(text[ip_pos + 6: ip_pos_end])




