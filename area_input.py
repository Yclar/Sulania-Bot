import requests
from bs4 import BeautifulSoup
import time
area_cnt = 0
prov = ([[0, 0] for x in range(0, 31)])
area = ([[0, 0] for x in range(0, 10001)])
r = requests.get('https://tianqi.moji.com/weather/china/')
soup = BeautifulSoup(r.text, 'html.parser')
tag = soup.find_all('li')
for i in range(0, 31, 1):
    prov[i][0] = tag[i].text
    prov[i][1] = 'https://tianqi.moji.com'+tag[i].find('a').attrs['href']
for i in range(0, 31, 1):
    time.sleep(1.5)
    r = requests.get(prov[i][1])
    soup = BeautifulSoup(r.text, 'html.parser')
    tag = soup.find_all('ul')[1].find_all('li')
    for x in tag:
        area_cnt += 1
        area[area_cnt][0] = x.get_text().replace('\n', '')
        area[area_cnt][1] = x.find('a').attrs['href']
f = open("area", "w", encoding='utf-8')
for i in range(1, area_cnt+1):
    f.write(area[i][0] + '#' + area[i][1] + '\n')
f.close()

