import requests

url = 'http://irs.thsrc.com.tw/IMINT/'
#自訂標題

headers = {
    'user-agent':'Mozilla/5.0 (windows NT 10.0; win64; x64)
    AppleWebKit/537.36 (KHTML like Gecko) Chrome/
    64.0.3282.186 safari/537.36'
}

html = request.get(url, headers = headers)

print(html)