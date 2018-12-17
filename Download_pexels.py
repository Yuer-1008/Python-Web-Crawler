__author__ = 'YFY'
'''
Pexel网站图片采集
https://www.pexels.com/
爬虫仅做为学习使用，无任何商业行为。
'''
# --*-- coding:utf-8 --*--

import requests
from bs4 import BeautifulSoup
from lxml import etree
import urllib.parse

url = "https://www.pexels.com/search/nature/"
header = {
#"Host":"sou.zhaopin.com",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0 Name",
#"Referer":"https://www.zhaopin.com/",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#"Accept-Encoding":"utf-8, gzip, deflate, sdch, br",
"Accept-Language":"zh-CN,zh;q=0.8",
"Connection":"keep-alive"
}

def buildUrl(key_word, num):
    word = urllib.parse.quote(string= key_word, encoding= 'utf-8')
    tar_url = "https://www.pexels.com/search/{word}/?page={num}".format(word = word, num = str(num))
    return tar_url

def Download(url, header):
    content = requests.get(url= url, headers = header).content
    html = etree.HTML(content)
    img_name = html.xpath('//img[@class="photo-item__img"]/@alt')
    img_URL = html.xpath('//img[@class="photo-item__img"]/@data-large-src')
    print(img_name)
    print(img_URL)
    # soup = BeautifulSoup(response.text , 'html.parser')
    # img_url = soup.find_all("img", attrs={'class':'photo-item__img'})#, attrs={'class':'red'})

    for i in range(len(img_name)):
        data = requests.get(url= img_URL[i], headers = header)
        with open('./photo/%s.jpeg' % img_name[i], "wb") as f:
            f.write(data.content)

if __name__ == "__main__":
    print("从Pexel网站批量下载照片.......")
    key_word = input("请输入搜索关键字：")
    print("=====每页30张图片")
    num = input("请输入页码：")
    for i in range(int(num)):
        index = i + 1
        url = buildUrl(key_word, index)
        Download(url, header)
