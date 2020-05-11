import requests


infos = requests.get('https://job.xiyanghui.com/api/q1/json').json()


def build(n, parent, dic):
    dic[n["id"]] = {"name": n["name"], "parent": parent}
    for i in n.get("children", []):
        build(i, n["id"], dic)


def builds(infos, dic):
    for i in infos:
        build(i, -1, dic)


def check(dic, id):
    if id not in dic:
        return '不存在'

    lst = []
    while id != -1:
        lst.append(dic[id]['name'])
        id = dic[id]["parent"]
    return '>'.join(lst[::-1])


dic = {}
builds(infos, dic)
print(check(dic, 1120))
print(check(dic, 2221))


##############################
# 请根据汇率接口实现 SDK 类，可提供方法，输入币种与价格，输出人民币相应的实时价格。
rates = requests.get('https://app-cdn.2q10.com/api/v2/currency').json()

class RateConverter:
    @staticmethod
    def convertToCNY(s):
        small = {j:i for i,j in [('USD', '$'),('GBP', '£'),('EUR', '€'),('HKD','HK$'),('JPY', '¥')]}
        coin = ''
        num = 0
        for index, c in enumerate(s):
            if c.isdigit():
                coin = s[:index]
                num = float(s[index:].replace(',', ''))
                if coin in small:
                    coin = small[coin]
                return num / rates['rates'][coin] * rates['rates']['CNY']
        return -1


for i in ['$1,999.00', 'HKD2399', 'EUR499.99', '€499.99']:
    print('输入 {}, 输出 {}'.format(i, RateConverter.convertToCNY(i)))