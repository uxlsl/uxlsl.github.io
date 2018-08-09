import requests

code = open('./tree.py', 'r').read()
info = {'username': '林松龄', 'tel': '18613077154', 'code': code}

r = requests.post('http://172.104,90.126:13000/answer', json=info)
print(r.text)
print(r.json())
