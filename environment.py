#抓取和讯网上市公司社会责任报告http://stockdata.stock.hexun.com/zrbg/Plate.aspx?date=2017-12-31
import re
import fake_useragent as fake
import requests
import pandas as pd

#生成模拟浏览器
ua=fake.UserAgent()
a=ua.random
headers={"User-Agent":a}


#设置年份、页数、个数
page=183
year='2016'
n=3650
#开始爬取
table=[]
y=[]
for j in range(8):
    for i in range(200):
        url='http://stockdata.stock.hexun.com/zrbg/data/zrbList.aspx?date={}-12-31&count=20&pname=20&titType=null&page={}'.format(j+2009,i+1)
        response=requests.get(url,headers=headers).text
        web_infor=re.findall(r'industry.*?(?=,Hstock)',response,re.S)
        for item in web_infor:
            table.append(item)
            y.append(j+2009)

#表格整理
industry,stockNumber,industryrate,Pricelimit,lootingchips,Scramble,rscramble,Strongstock=[],[],[],[],[],[],[],[]
for item in table:
    string=str(item)
    industry.append(re.findall(r'(?<=industry:\').*?(?=\')',string)[0])
    stockNumber.append(eval(re.findall(r'(?<=stockNumber:\').*?(?=\')',string)[0]))
    industryrate.append(eval(re.findall(r'(?<=industryrate:\').*?(?=\')',string)[0]))
    Pricelimit.append(re.findall(r'(?<=Pricelimit:\').*?(?=\')',string)[0])
    lootingchips.append(eval(re.findall(r'(?<=lootingchips:\').*?(?=\')',string)[0]))
    Scramble.append(eval(re.findall(r'(?<=Scramble:\').*?(?=\')',string)[0]))
    rscramble.append(eval(re.findall(r'(?<=rscramble:\').*?(?=\')',string)[0]))
    Strongstock.append(eval(re.findall(r'(?<=Strongstock:\').*?(?=\')',string)[0]))


#存入文件
data=pd.DataFrame({'year':y,'name':industry,'score':industryrate,'rate':Pricelimit,'shareholder':stockNumber,'employee':lootingchips,'supplier_customer':Scramble,'environment':rscramble,'society':Strongstock})
data.to_excel(r'D:\\何伟\\中南财研究生\\论文\\沪港通和环境\\environment.xlsx',sheet_name='sheet1')

    
