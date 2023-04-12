# -*- coding: utf-8 -*-
# author: renmjchn
import requests
from bs4 import BeautifulSoup
import os
from tqdm import tqdm
import urllib3


requests.packages.urllib3.disable_warnings()


def dl_pic(url, tt):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'}
    res = requests.request('GET', url, headers=headers, verify=False)
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('img', class_="zoom")
    name = tt
    pbar = tqdm(range(len(links)), desc=name)
    if os.path.exists('pics'):
        pass
    else:
        os.mkdir('pics')
    for i in links:
        pbar.update(1)
        soup2 = BeautifulSoup(str(i), 'html.parser')
        link = soup2.img['file']
        res2 = requests.request('GET', link, headers=headers, verify=False)
        cont = res2.content
        path = 'pics\\' + tt
        if os.path.exists(path):
            pass
        else:
            os.mkdir(path)
        with open(path + '\\' + str(links.index(i)) + '.jpg', 'wb+') as f:
            f.write(cont)
    pbar.close()



def dl_pic_one_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'}
    res = requests.request('GET', url, headers=headers, verify=False)
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    dic = soup.find_all('a', class_='s xst')[4:]
    for i in dic:
        soup2 = BeautifulSoup(str(i), 'html.parser')
        title = soup2.a.string
        link = site + soup2.a['href']
        dl_pic(link, title)


if __name__ == '__main__':
    site = 'https://www.sehuatang.org/'
    num = int(input('请输入需要下载的页数，默认从第1页开始下载：'))
    for i in range(num):
        url = 'https://www.sehuatang.org/forum-98-%s.html' % (str(i + 1))
        dl_pic_one_page(url)
    print('全部下载完成！')