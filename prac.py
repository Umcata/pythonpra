import telepot
import sys
import io
import time
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
import requests
from bs4 import BeautifulSoup
token = "5099349768:AAGAbf0A13AWLhj059buIfVn-_gwq3Afw_s"
bot = telepot.Bot(token)
id = "-1001574116637"

url = "https://news.daum.net/ranking/popular"
# res = requests.get(url)
# res.raise_for_status()
# soup = BeautifulSoup(res.content,'lxml')
# pra = soup.select_one("#mArticle > div.rank_news > ul.list_news2 > li:nth-child(2) > div.cont_thumb > strong > a")

# for i in range(1,11):
#     res = requests.get(url)
#     res.raise_for_status()
#     soup = BeautifulSoup(res.content,'lxml')
#     urlrank = f"#mAside > div.aside_g.aside_ranking > ul > li.on > div > ol:nth-child(2) > li:nth-child({i}) > strong > a"
#     pra = soup.select_one(urlrank)
#     (pra.text[40:-20])

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.content,'lxml')
urlrank1 = "#mAside > div.aside_g.aside_ranking > ul > li.on > div > ol:nth-child(2) > li:nth-child(1) > strong > a"
urlrank2 = "#mAside > div.aside_g.aside_ranking > ul > li.on > div > ol:nth-child(2) > li:nth-child(2) > strong > a"
urlrank3 = "#mAside > div.aside_g.aside_ranking > ul > li.on > div > ol:nth-child(2) > li:nth-child(3) > strong > a"
urlrank4 = "#mAside > div.aside_g.aside_ranking > ul > li.on > div > ol:nth-child(2) > li:nth-child(4) > strong > a"
urlrank5 = "#mAside > div.aside_g.aside_ranking > ul > li.on > div > ol:nth-child(2) > li:nth-child(5) > strong > a"
urlrank6 = "#mAside > div.aside_g.aside_ranking > ul > li.on > div > ol:nth-child(2) > li:nth-child(6) > strong > a"
urlrank7 = "#mAside > div.aside_g.aside_ranking > ul > li.on > div > ol:nth-child(2) > li:nth-child(7) > strong > a"
urlrank8 = "#mAside > div.aside_g.aside_ranking > ul > li.on > div > ol:nth-child(2) > li:nth-child(8) > strong > a"
urlrank9 = "#mAside > div.aside_g.aside_ranking > ul > li.on > div > ol:nth-child(2) > li:nth-child(9) > strong > a"
urlrank10 = "#mAside > div.aside_g.aside_ranking > ul > li.on > div > ol:nth-child(2) > li:nth-child(10) > strong > a"
pra1 = soup.select_one(urlrank1)
pra2 = soup.select_one(urlrank2)
pra3 = soup.select_one(urlrank3)
pra4 = soup.select_one(urlrank4)
pra5 = soup.select_one(urlrank5)
pra6 = soup.select_one(urlrank6)
pra7 = soup.select_one(urlrank7)
pra8 = soup.select_one(urlrank8)
pra9 = soup.select_one(urlrank9)
pra10 = soup.select_one(urlrank10)

allcon = f"1. {pra1.text[40:-30]}\n \
2. {pra2.text[40:-30]}\n \
3. {pra3.text[40:-30]}\n \
4. {pra4.text[40:-30]}\n \
5. {pra5.text[40:-30]}\n \
6. {pra6.text[40:-30]}\n \
7. {pra7.text[40:-30]}\n \
8. {pra8.text[40:-30]}\n \
9. {pra9.text[40:-30]}\n \
10. {pra10.text[40:-30]}\n"

whatday = time.strftime('%Y-%m-%d', time.localtime(time.time()))
daumlink = "https://news.daum.net/ranking/popular"
bot.sendMessage(id, f"{whatday}\nDaum 뉴스 랭킹 top 10!" +"\n\n"+ allcon + f"\n 더보기... {daumlink}")