import requests
from bs4 import BeautifulSoup

url = "https://zhihu.com"

# 发送HTTP请求
response = requests.get(url)

# 解析HTML
soup = BeautifulSoup(response.text, "html.parser")

# 获取页面标题
title = soup.title.string

# 打印页面标题
print(title)
