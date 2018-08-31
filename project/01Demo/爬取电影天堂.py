#爬虫，爬取电影天堂资源http://www.dytt8.net/html/gndy/dyzz/list_23_1.html，数字1是页码
import requests
import json # 解析json数据
import pymysql
from bs4 import BeautifulSoup #解析html标签

#向数据库插入数据
def setSql(imgsrc,flburl,nickname,name,category,synopsis):
    conn = pymysql.connect(host='localhost',port=3306,db='test',user='root',passwd='123456',charset='utf8')
    cur = conn.cursor()
    try:
        sql = "insert into tb_dytt(imgsrc,flburl,nickname,name,category,synopsis) values('{0}','{1}','{2}','{3}','{4}','{5}')".format(imgsrc,flburl,nickname,name,category,synopsis)
        cur.execute(sql)
        conn.commit()
    except:
        conn.rollback()
        print('插入信息错误')
        raise
    finally:
        cur.close()
        conn.close()



#爬取详情页
def getDetails(Detailsurl):
    #爬取详情页
    res = requests.get(Detailsurl)
    res.encoding = 'gbk' #字符编码转换
    myhtml = res.text
    soup = BeautifulSoup(myhtml  ,'html.parser')
    myclass= soup.select('#Zoom')  #根据class获得标签 返回list

    #获取简介信息

    # textobj = myclass[0].find_all('p')
    # for item in textobj:
    #     textsum = item.text.find('◎译　　名') #获取a标签的属性值，并判断是否包含磁链接
    #     if textsum >= 0:
    #         print(item.text)


    textobj = myclass[0].find_all('span')
    for item in textobj:
        textsum = item.text.find('◎译　　名') #获取a标签的属性值，并判断是否包含磁链接
        if textsum >= 0:
            print(item.text.replace('\n','#'))
            break
     # print(item.text.replace('\\n',''))
















    # print(myclass[0])
    #获取电影海报地址
    # myimg = myclass[0].find('img')
    # imgsrc = myimg['src']
    # print(imgsrc)

    #获取下载磁链接
    # ftpobj = myclass[0].find_all('a') #找到下面的所有a标签
    # for item in ftpobj:
    #     flbsum = item['href'].find('ftp://') #获取a标签的属性值，并判断是否包含磁链接
    #     if flbsum >= 0:
    #         print(item['href'])



    return
    #获取基本信息
    mystr = mytext[0].text
    mystr = mystr.replace(' ','').replace('【下载地址】磁力链下载点击这里','').replace('影片截图:','') #替换字符串
    mystr = mystr.replace('　　','').replace('　','')
    yiming =  mystr.find('◎译名')
    pianming = mystr.find('◎片名')
    niandai = mystr.find('◎年代')
    leibie = mystr.find('◎类别')
    yuyan = mystr.find('◎语言')
    jianjie = mystr.find('◎简介')

    nickname = mystr[yiming+3:pianming] #得到译名
    name = mystr[pianming+3:niandai] #得到片名
    category = mystr[leibie+3:yuyan] #得到类别
    synopsis = mystr[jianjie+3:] #得到简介
    print(imgsrc)
    print(flburl)
    print(nickname)
    print(name)
    print(category)
    print(synopsis)
    setSql(imgsrc,flburl,nickname,name,category,synopsis) #数据库写入数据

#爬取目录页
def getlist(lsiturl):
    res = requests.get(lsiturl)
    res.encoding = 'gbk' #字符编码转换
    myhtml = res.text
    soup = BeautifulSoup(myhtml  ,'html.parser')
    myclass= soup.select('.ulink')  #根据class获得标签 返回list
    for item in myclass:
        myurl = 'http://www.dytt8.net'+item['href']
        getDetails(myurl) #抓取详情页


def executeFun():
    url = 'http://www.dytt8.net/html/gndy/dyzz/list_23_1.html'
    getlist(url) #抓取列表页

# Detailsurl = 'http://www.dytt8.net/html/gndy/dyzz/20180718/57148.html'#首页
Detailsurl = 'http://www.dytt8.net/html/gndy/dyzz/20091004/22009.html'#尾页
# Detailsurl = 'http://www.dytt8.net/html/gndy/dyzz/20091004/22030.html'#倒数第二页
getDetails(Detailsurl)
# executeFun()

















'''
mystr = res.text.lstrip('jQuery183009375593461432796_1530973514210(').rstrip(')') #将返回的数据截取成json字符串
print(mystr)
mystr = mystr.replace('<p>',' ') #替换字符串
mystr = mystr.replace('</p>',' ')
mystr = mystr.replace('\\r',' ')  # 字符传中不能包含\r
jd = json.loads(mystr) #将json字符串转成python字典
print(jd)
print(jd['chapter']['htmlContent'])
'''

'''
myhtml = '<a class= "myclass" id = "myid" mydata="自定义属性">显示</a>'
soup = BeautifulSoup(myhtml  ,'html.parser')
print(soup)
#可以根据标签类、id等查找信息,如下：
mya= soup.select('a')  #获得a标签  返回list
myclass= soup.select('.myclass')  #根据class获得标签 返回list
myid= soup.select('#myid')  #根据id获得标签 返回list
print(mya[0].text)  #获得a标签中的内容：显示
print(mya[0]['mydata'])  #获得a标签中的mydata属性内容：自定义属性

'''


