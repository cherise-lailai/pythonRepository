# -*- coding: utf-8 -*-
import requests
# 使用urlencode将key-value这样的键值对转换成我们想要的格式，返回的是a=1&b=2这样的字符串。
from urllib.parse import urlencode
from requests.exceptions import RequestException
# reponce使用Content-Encoding=br压缩，所以需要brotli模块用于解压
import brotli
# 将json文件保存到本地XXX.json，再次读取将json字符串转换为对应的python数据类型（load 方法），主要是{}对象转dict,[]数组转list
import json
import sqlite3
# sqllite3的数据库位置
conn = sqlite3.connect('D:\\Program Files\\sqlite\\data\\智联招聘福州（java_python）\\jobData.db')
# get方式提交的参数字典
param={
    'start':180,
    'pageSize':60,
    'cityId':681,
    'workExperience':-1,
    'education':-1,
    'companyType': -1,
    'employmentType': -1,
    'jobWelfareTag': -1,
    'kw': 'python',
    'kt': 3,
    'lastUrlQuery': {"p":4,"pageSize":"60","jl":"681","kw":"python","kt":"3"}
}
# http协议中request请求的请求头信息，数值可以使用本地浏览器开发者工具（F12）查看并修改
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Host': 'fe-api.zhaopin.com',
    'Referer': 'https://sou.zhaopin.com/?p=4&pageSize=60&jl=681&kw=python&kt=3',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Origin': 'https://sou.zhaopin.com',
    # cookie 修改为(本地的cookie,爬取前我先登入了，省得麻烦)
    'Cookie':''
}

def getPage(city='',keyword='',pageNo=4):
    param['start']=60*(pageNo-1)
    param['kw']=keyword
    tempDict={"p":4,"pageSize":"60","jl":"681","kw":"python","kt":"3"}
    tempDict['p']=pageNo
    tempDict['kw']=keyword
    # print(tempDict)
    param['lastUrlQuery']=tempDict
    # print(str(tempDict))
    # print(param)
    # print(urlencode(param))
    url = 'https://fe-api.zhaopin.com/c/i/sou?' + urlencode(param)
    try:
        # 获取网页内容，返回html数据
        response = requests.get(url, headers=headers)
        # 通过状态码判断是否获取成功
        # print(response.encoding)
        # print(response.headers)
        # print(response.headers['Content-Encoding'])  Content-Encoding=br
        # 此处必须使用brotli进行解压，否者为乱码，其中brotli模块安装可能失败，提示microsoft visual c++ 14.0 is required，可以通过安装解决
        tempData = brotli.decompress(response.content)
        data = tempData.decode('utf-8')
        filename='智联_'+city+'_'+keyword+'_第'+str(pageNo)+'頁_数据.json'
        with open(filename,'w',encoding='utf-8')as f:
            f.write(data)
            # print(data)
        if response.status_code == 200:
            return data
        return None
    except RequestException as e:
        return None
def savToSqlite(keyword,pageNo):
    for i in range(1,pageNo+1):
        filename='智联_福州_'+keyword+'_第'+str(i)+'頁_数据.json'
        with open(filename,'r',encoding='utf-8') as f:
            data=f.read()
        dataJson = json.loads(data)
        dataList=dataJson['data']['results']
        print(dataList)
        dataListLength = len(dataJson['data']['results'])
        for record in dataList:
            number=keyword+'_'+record['number']
            jobType = record['jobType']['display']
            companyName=record['company']['name']
            company_size=record['company']['size']['name']
            company_type=record['company']['type']['name']
            workingExp=record['workingExp']['name']
            eduLevel = record['eduLevel']['name']
            salary=record['salary']
            emplType= record['emplType']
            jobName=record['jobName']
            city=record['city']['display']
            welfare=','.join(record['welfare'])  #列表字符串
            timeState=record['timeState']
            # print(number,jobType,companyName,company_size,company_type,workingExp,eduLevel,salary,emplType,jobName,city,welfare,timeState,keyword)
            insertSql='insert into recruitment(number,jobType,companyName,company_size,company_type,workingExp,' \
                      'eduLevel,salary,emplType,jobName,city,welfare,timeState,keyword) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
            conn.execute(insertSql,(number,jobType,companyName,company_size,company_type,workingExp,eduLevel,salary,emplType,jobName,city,welfare,timeState,keyword))
            conn.commit()
    # number
    # jobType
    # companyName
    # company_size
    # company_type
    # workingExp
    # eduLevel
    # salary
    # emplType
    # jobName
    # city,
    # welfare
    # timeState

if __name__ == '__main__':
    # 由于爬取数据时，发现python才7页，java远多于7页，所以为了便于处理比较，将数据爬取页数设置为7
    totalPage=7
    # 下载json文件
    # for pageNo in range(1,totalPage+1):
    #     html=getPage('福州','java',pageNo)
    # 保存到数据库
    savToSqlite('python',totalPage)
    savToSqlite('java',totalPage)