# 引入python 爬虫基本需要的库
import requests
# 创建url
url = "https://www.baidu.com/"

# 发送请求，使用get方法发送请求
respose = requests.get(url)
# 获得文本类容,并将文件转化成UTF-8的编码格式
respose.encoding="utf-8"

content = respose.text

print(content)