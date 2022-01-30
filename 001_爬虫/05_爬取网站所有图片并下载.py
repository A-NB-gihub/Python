import requests
import re

url = "http://www.gaokao.com/gkpic/"

resp = requests.get(url)
html = resp.content.decode("gbk")
# 正则表达式，详细百度
# <img src="(.*)" alt=".*"> 小括号内为提取出来需要的内容， .表示任意字符 *表示出现任意次数
urls = re.findall('<img src="(.*)" alt=".*"> ', html)
names = re.findall('<img src=".*" alt="(.*?)">', html)
# print(names)
for i in range(0, len(urls)):
    with open('./data/img/' + str(names[i]) + '.jpg', 'wb') as file:
        resp = requests.get(urls[i])
        file.write(resp.content)
        print("第{}已下载".format(i))