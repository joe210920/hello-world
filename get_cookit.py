import requests
url = 'http://www.ptt.cc/bbs/Gossiping/index.html'
#設定cookies的值
cookies = {'over18' : '1'}
r = requests.get(url, cookies = cookies)
print(r.text)
#結果:通過認證，取到目標網頁內容