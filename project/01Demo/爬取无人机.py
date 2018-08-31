# 抓取航拍图片和视频，以及360全景图时 https://www.skypixel.com/explore
import requests
import json # 解析json数据
import pymysql
import sys
import time


#向数据库插入数据
def setSql(urlpath,urltype,time):
    conn = pymysql.connect(host='localhost',port=3306,db='test',user='root',passwd='123456',charset='utf8')
    cur = conn.cursor()
    try:
        sql = "insert into tb_godimgurl(url,urltype,creatorTime) values('{0}','{1}','{2}')".format(urlpath,urltype,time)
        cur.execute(sql)
        conn.commit()
    except:
        conn.rollback()
        print('插入信息错误')
        raise
    finally:
        cur.close()
        conn.close()




def geturl(url,stoptext,time):
    urlpath=url
    res = requests.get(urlpath)
    res.encoding = 'utf-8'
    mystr = res.text
    jd = json.loads(mystr) #将json字符串转成python字典
    if ("data" in jd.keys()):
        mydata = jd['data']['items']
        for item in mydata:
            if item['type'] == 'photo':
                myurl = item['slug']
                if myurl == stoptext:
                    print('退出')
                    sys.exit(0)
                photouri = 'https://www.skypixel.com/photos/{0}'.format(myurl)
                setSql(photouri,1,time)
                print(photouri)
            if item['type'] == 'video':
                myurl = item['slug']
                if myurl == stoptext:
                    print('退出')
                    sys.exit(0)
                photouri = 'https://www.skypixel.com/videos/{0}'.format(myurl)
                setSql(photouri,2,time)
                print(photouri)
            if item['type'] == 'photo_360':
                myurl = item['slug']
                if myurl == stoptext:
                    print('退出')
                    sys.exit(0)
                photouri = 'https://www.skypixel.com/photos/{0}'.format(myurl)
                setSql(photouri,3,time)
                print(photouri)
def zhiXing():
    sum = 0
    for i in range(0,257):
        strurl = 'https://www.skypixel.com/api/v2/works?lang=zh-CN&platform=web&sort=hot&filter=featured:true&limit=20&offset={0}'.format(sum)
        sum+=20
        geturl(strurl,'sea-ghosts','2018-08-05') #参数1：所查询的URL，参数2：避免查询重复数据，参数3：指定查询的时间，用于标记查询记录
        print(i)
        print(sum)
       # time.sleep(5)
zhiXing()
