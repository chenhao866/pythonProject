#根据数据库无人机数据，查询详细数据
import requests
from bs4 import BeautifulSoup #解析html标签
import pymysql
import random

#查询MYSQL
def querysql():
    conn = pymysql.connect(host='localhost',port=3306,db='test',user='root',passwd='123456',charset='utf8')
    cur = conn.cursor()
    sql = "select * from tb_godimgurl"
    try:
        cur.execute(sql)
        # result = cur.fetchone()
        result = cur.fetchall()
        return result
    except:
        conn.rollback()
        return '错误'
        print('查询信息错误')
    finally:
        cur.close()
        conn.close()
def getSqlUrl():
    result = querysql() #查询得到数据库数据
    if result != '错误':
        for data in result:
            sumtype = data[2]
            myurl = data[1]
            print(data)
#单张    https://www.skypixel.com/api/v2/photos/sea-ghosts?lang=zh-CN&platform=web&device=desktop&compatible=true
url1 = 'https://www.skypixel.com/photos/sea-ghosts'

#专辑   https://www.skypixel.com/api/v2/photos/dji-0431-hdr-674ac805-3935-4efe-bd12-00c6c719a67e?lang=zh-CN&platform=web&device=desktop&compatible=true
url2 ='https://www.skypixel.com/photos/dji-0431-hdr-674ac805-3935-4efe-bd12-00c6c719a67e'

#视频   https://www.skypixel.com/api/v2/videos/vlog2-79f121df-82be-4931-9ba0-df811e6a05b7?lang=zh-CN&platform=web&device=desktop
url3 ='https://www.skypixel.com/videos/vlog2-79f121df-82be-4931-9ba0-df811e6a05b7'

#全景 https://www.skypixel.com/photos/play/sun-rise-malta?buttons=on
url4 ='https://www.skypixel.com/photos/sun-rise-malta'


def getheaders():
    user_agent_list = [ \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1" \
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", \
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", \
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", \
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", \
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    UserAgent=random.choice(user_agent_list)
    headers = {'User-Agent': UserAgent}
    return headers
headers = getheaders() # 定制请求头
res = requests.get('https://www.skypixel.com/photos/sun-rise-malta',headers=headers)
res.encoding = 'utf-8'
mystr = res.text
print(mystr)
