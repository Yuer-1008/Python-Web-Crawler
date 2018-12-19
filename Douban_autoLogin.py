# --*-- coding:utf-8 --*--
__author__ = 'YFY'
'''
豆瓣自动登录(需要完善无图片验证码如何操作)
'''

import re
from bs4 import BeautifulSoup
import requests

loginurl = "https://www.douban.com/accounts/login"

header = {
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0 Name",
#"Referer":"http://blog.sina.com.cn/",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#"Accept-Encoding":"gzip, deflate, sdch",
"Accept-Language":"zh-CN,zh;q=0.8",
"Connection":"keep-alive"
}
proxy = {
    "http": "http://{}:{}".format("182.88.88.124", "8123"),
    "https": "https://{}:{}".format("210.22.176.146", "32153")
}

# data = {
#     'source':'index_nav',
#     'redir':'https://www.douban.com/',
#     'form_email':'18315507873',
#     'form_password':'yfy19921008',
#     'login':'登录'
# }

# 豆瓣自动登录函数
def douban_autologin(loginurl, header):
    login_response  = requests.get(url= loginurl, headers = header).text
    #print(login_response)
    pat = 'class="item item-captcha"'   #判断是否有验证码的关键字
    result = re.search(pat, login_response)
    print(result)
    if str(result) == 'None':
        data = {
            'source':'index_nav',
            'redir':'https://www.douban.com/',
            'form_email':'18315507873',
            'form_password':'yfy19921008',
            'login':'登录'
        }
    else:
        verifyCodeUrl = re.compile('<img id="captcha_image" src="(.*?)" alt="captcha"', re.S).findall(login_response)[0]
        captcha_id = re.compile('name="captcha-id" value="(.*?)"/>', re.S).findall(login_response)[0]
        verifyResponse = requests.get(url= verifyCodeUrl, headers = header).content

        with open("im_code.jpg",'wb') as f:
            f.write(verifyResponse)

        captcha_solution = input("请输入验证码：")

        data = {
            'source':'index_nav',
            'redir':'https://www.douban.com/',
            'form_email':'18315507873',
            'form_password':'yfy19921008',
            'captcha-solution':captcha_solution,
            'captcha-id': captcha_id,
            'login':'登录'

        }

    LoginPost = requests.post(url= loginurl, data= data, headers = header)
    # 验证是否登录成功
    soup = BeautifulSoup(LoginPost.content, 'html.parser')
    result_title = soup.find_all('div', attrs={'class': 'title'})
    for k in result_title:
        result_title_text = k.find('a').get_text()
        print(result_title_text)

if __name__ == '__main__':
    douban_autologin(loginurl, header)