'''
import requests
#將查詢參數定義為字典資料加入get中
payload = {'key1' : 'value1', 'key' : 'value2'}
html = requests.get("http://httpbin.org/get", params = payload)
#print(r.text)
'''
import requests

#將查詢參數加入post當中 
payload = {"key1" : "value1", "key2" : "value2"}
html - request.post("http://httpbin.org/post", data = payload)
print(r.text)
