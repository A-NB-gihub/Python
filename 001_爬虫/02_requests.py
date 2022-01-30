import requests

# url = "https://www.baidu.com"
# resp = requests.get(url)

# content 二进制字节码
# 使用resp.text会乱码
# print(resp.content.decode("UTF-8")) 用UTF-8重编码
# print(resp.encoding) 解码编码

# 伪装设备信息绕过反爬
# User-Agent 浏览器标识，python默认为python-requests，可被识别并禁止访问
# url = "https://www.zhihu.com/"
# header = {
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
# }
# resp = requests.get(url, headers=header)
# print(resp.text)

# params参数
# url1 = "https://www.antvv.com?id=14"
# url2 = "https://www.antvv.com"
# params = {
#     "id": 14
# }
# header = {
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
# }
# resp = requests.get(url2, params=params, headers=header)    #等同resp = requests.get(url1)，部分网站需要用传参数的方法才能获取
# print(resp.text)


# 请求资源文件（下载文件）
# 视频，用流文件（steam下载减小内存占用
# url = "https://yinghua-oss.njc.svp.tencent-cloud.com/yinghua_0bcajqaaeaaa6eacklg2xzqxktgdajgaaasa.f0.mp4?dis_k=f38b7a27139647e8ce6adaeb580cf44a&dis_t=1641692491"
# resp = requests.get(url, stream=True)
# with open("./data/xxx.mp4", "wb") as file:    # 注意参数保存类型 wb二进制 w文本，类型可用print(type(resp.content))查看
#     for j in resp.iter_content(1024*10):    # 参数：每次读取字节数，这里表示每次读10k，循环写到本地文件
#         file.write(j)
# 图片
url = "https://ae01.alicdn.com/kf/H458e88d22ad84951a82157684234895cP.jpg"
resp = requests.get(url)
with open("./data/xxxx.png", "wb") as file:
    file.write(resp.content)


