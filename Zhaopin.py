__author__ = 'YFY'
'''
智联招聘网站数据采集
https://www.zhaopin.com/
'''
import requests
import json
import xlwt

book = xlwt.Workbook()
sheet = book.add_sheet('sheet_yfy', cell_overwrite_ok= True)

num = 0     # 搜索结果开始
tar_url = "https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=90&cityId=664&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python%E5%BC%80%E5%8F%91&kt=3&_v=0.28065343&x-zp-page-request-id=8db8b1892d6c4762acbc561818ab7c1b-1544917823851-394146".format(num)# + str(page)
header = {
"Host":"sou.zhaopin.com",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0 Name",
"Referer":"https://www.zhaopin.com/",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#"Accept-Encoding":"utf-8, gzip, deflate, sdch, br",
"Accept-Language":"zh-CN,zh;q=0.8",
"Connection":"keep-alive"
}
content = requests.get(url= tar_url, headers = header).text
json_content = json.loads(content)
# json_text = json.dumps(json_content, indent= 4, separators=(',',':'), ensure_ascii = False)
# with open('json.txt', 'w') as f:
#     f.write(json_text)
company_name = []
workingExp = []
eduLevel = []
salary = []
emplType = []
jobName = []
city = []
welfare = []

for i in range(len(json_content["data"]["results"])):
    company_name.append(json_content["data"]["results"][i]["company"]["name"])
    workingExp.append(json_content["data"]["results"][i]["workingExp"]["name"])
    eduLevel.append(json_content["data"]["results"][i]["eduLevel"]["name"])
    salary.append(json_content["data"]["results"][i]["salary"])
    emplType.append(json_content["data"]["results"][i]["emplType"])
    jobName.append(json_content["data"]["results"][i]["jobName"])
    city.append(json_content["data"]["results"][i]["city"]["display"])
    welfare.append(json_content["data"]["results"][i]["welfare"])
j = 0
for i in range(len(company_name)):
    try:
        sheet.write(i+1,j+7, emplType[i])
        sheet.write(i + 1, j+1, company_name[i])
        sheet.write(i + 1, j+2, salary[i])
        sheet.write(i + 1, j+3, city[i])
        sheet.write(i + 1, j+4, workingExp[i])
        sheet.write(i + 1, j+5, eduLevel[i])
        sheet.write(i + 1, j+6, welfare[i])
        sheet.write(i + 1, j, jobName[i])
    except Exception as e:
        print("出现异常" + str(e))
        continue

book.save('Test.xls')



#print(len(company_name))
# file = open('test.json', 'w')
# for i in content:
#     json_i = json.dumps(i)
#     file.write(json_i + '\n')
# file.close()


# html = etree.HTML(content)
# result1 = html.xpath('//span[@class="contentpile__content__wrapper__item__info__box__jobname__title"]/text()')
#print(json_content['data']['results'])


# content = requests.get(url= url, headers = header).content
# html = etree.HTML(content)
# element = html.xpath('//img[@class="photo-item__img"]/@data-large-src')
# for ele in element:
#     print(type(ele))

# soup = BeautifulSoup(response.text , 'html.parser')
# img_url = soup.find_all("img", attrs={'class':'photo-item__img'})#, attrs={'class':'red'})
#
# for val in img_url:
#     img_name = val.get('alt')
#     img_URL = val.get('data-large-src')
#     data = requests.get(url= img_URL)
#     #img_source = bytes(val.get('data-large-src'), encoding= 'utf-8')
#     with open('./photo/%s.jpeg' % img_name, "wb") as f:
#         f.write(data.content)
#
# for val in img_url:
#     print(val.get('data-big-src'))
#     #print(val.get('data-big-src'))

