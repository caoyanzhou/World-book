import requests
from bs4 import BeautifulSoup

fanhao = input('请输入番号：')
url = f'https://faleno.jp/top/works/{fanhao}'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    image_tag = soup.find('a', {'class': 'pop_sample'}).find('img')
    if image_tag:
        image_url = image_tag['src']
        image_url = image_url.split('?')[0]
        print(f'影片{fanhao}的海报地址为：{image_url}')
    else:
        print(f'未能找到影片{fanhao}的海报')
else:
    print(f'无法连接到Faleno网站，请检查您的网络连接或稍后再试')
