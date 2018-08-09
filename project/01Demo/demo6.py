#抓取百度图片风景图片
import requests
import json # 解析json数据
import pymysql

#向数据库插入数据
def setSql(imgpath,text):
    conn = pymysql.connect(host='localhost',port=3306,db='test',user='root',passwd='123456',charset='utf8')
    cur = conn.cursor()
    try:
        sql = "insert into tb_img(imgpath,text) values('{0}','{1}')".format(imgpath,text)
        cur.execute(sql)
        conn.commit()
    except:
        conn.rollback()
        print('插入信息错误')
        raise
    finally:
        cur.close()
        conn.close()

def getimg(urlpath):
    res = requests.get(urlpath)
    res.encoding = 'utf-8'
    mystr = res.text
    jd = json.loads(mystr) #将json字符串转成python字典
    mydata = jd['data']
    for myda in mydata:
        if ("thumbURL" in myda.keys()):
            text = myda['fromPageTitleEnc']
            imgpath = myda['thumbURL']
            mysss = "insert into con_map(CON_HPYS,CON_HPHM) values('{0}','{1}')".format(text,imgpath)
            print(text)
            print(mysss)
            setSql(imgpath,text)

def zhiXing():
    sum = 30
    for i in range(1,101):
        strurl = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E8%88%AA%E6%8B%8D%E9%A3%8E%E6%99%AF&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%E8%88%AA%E6%8B%8D%E9%A3%8E%E6%99%AF&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn={0}&rn=30'.format(sum)
        sum+=30
        getimg(strurl)
        print(strurl)
zhiXing()



