import sys

import xml.etree.ElementTree as ET

# xml_obj = ET.parse("files/newsafr.xml")
parser = ET.XMLParser(encoding="utf-8")
xml_obj = ET.parse("C:\Users\Ingvar\PycharmProjects\pythonProject\\newsafr.xml", parser)
root = xml_obj.getroot()

print(root.tag, root.text, root.attrib)

# news_list = root.find_all("channel/item")
# for news in news_list:
# 	print(news.find("title").text)

title_list = root.findall("channel/item/title")
for title in title_list:
	print(title.text)

sys.exit()


from pprint import pprint

import json

with open('C:\Users\Ingvar\PycharmProjects\pythonProject\\newsafr.json') as f:
	json_data = json.load(f)
news_list = json_data["rss"]["channel"]["items"]
for news in news_list:
	print(news["title"])

# pprint(news_list[0])

with open("C:\Users\Ingvar\PycharmProjects\pythonProject\\newsafr.json", "w") as f:
	json.dump(json_data, f, ensure_ascii=False, indent=4)

sys.exit()

import csv

with open("C:\Users\Ingvar\PycharmProjects\pythonProject\\newsafr.csv") as f:
	reader = csv.reader(f)
	# print(type(reader))
	# count = 0
	# for r in reader:
	# 	count += 1
	# 	print(type(r), r)
		# print(r[-1])
	news_list = list(reader)
	# reader = csv.DictReader(f)
	# for r in reader:
	# 	print(r["title"])
# print(len(news_list))
# print(news_list[1])

# print(f"Всего статей: {count-1}")
csv.register_dialect("customcsv", delimiter=",", quoting=csv.QUOTE_NONE, escapechar="\\")
with open("C:\Users\Ingvar\PycharmProjects\pythonProject\\newsafr.csv", "a") as f:
	writer = csv.writer(f, "customcsv")
	writer.writerows(news_list)