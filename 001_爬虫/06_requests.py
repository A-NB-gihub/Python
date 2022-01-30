import requests

# 请求 requests = requests.get(url, headers=, params=, stream=Bool)
# url 网址，协议://网址
# headers 消息头，User-Agent（用户标识），Referer（来源页）
# params 参数，也可加？拼在url后
# stream 是否用流传输，主要用于视频，开启的话只得到返回的消息头，内容部分一部分一部分的下载

#proxies 设置代理
# timeout 设置超时的时间，单位秒
# verify 是否强制验证证书


# 返回 response
# status_code 返回的状态码
# encoding 网页的编码
# text 网页的源代码，可以自动解析中文，可能乱码
# content 返回内容的字节码，可以使用decode解析中文
# json() 把json字符串变成python的数据类型

import json
# json->python 把json转换为python json.loads()
# python->json 把python转换为json json.dumps()

# json_str = '{"name":"小明","age":"19"}'
# print(json_str)
# json_python = json.loads(json_str)
# print(json_python)
#
# infos = {"chinese":80, "math":90}
# str1 = json.dumps(infos)
# print(type(str1))
# print(type(infos))

# 设置代理和超时时间
url = "http://httpbin.org/get"
proxies = {
    "http": "103.37.141.69:80"
}
r = requests.get(url, proxies=proxies, timeout=5)
result = r.json()
print(result["origin"])

