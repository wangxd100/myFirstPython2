import requests

headers = {'user-agent': 'my-app/0.0.1'}
url = "https://news.baidu.com"
text = requests.get(url)
print(text)
print(text.status_code)

r = requests.get(url, headers=headers)
print(r)




# pass parameters
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)

print(r.url)

# response content
j = requests.get('https://api.github.com/events')
print(r.text)