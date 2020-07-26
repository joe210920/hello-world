import requests
from bs4 import BeautifulSoup
'''
headers = {
    'content-type': 'text/html; charset=UTF-8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
'''
url = 'https://www.taiwanlottery.com.tw/'
r = requests.get(url)
html  = r.content
sp = BeautifulSoup(html, 'html.parser')

#找到威力彩的區塊
datas = sp.find('div', class_ = 'contents_box02')

#開獎期數
title = datas.find('span', 'font_black15').text
print('威力彩期數:', title)

#開獎號碼
nums = datas.find_all('div', class_= 'ball_tx ball_green')

#開出順序
print('開出順序:', end = " ")

for i in range(0, 6):
    print(nums[i].text, end = '')

#大小順序
print('\n大小順序:', end = ' ')

for i in range(6, 12):
    print(nums[i].text, end = ' ')

#第二區

num = datas.find('div', class_ = 'ball_red').text
print('\n第二區:', num)

