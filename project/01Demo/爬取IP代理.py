#ip    http://www.xicidaili.com/nn/2
import random
import requests
import pymysql
from bs4 import BeautifulSoup #解析html标签

#向数据库插入数据
def setSql(myip,myport,mytype):
    conn = pymysql.connect(host='localhost',port=3306,db='test',user='root',passwd='123456',charset='utf8')
    cur = conn.cursor()
    try:
        sql = "insert into tb_myip(myip,myport,mytype) values('{0}','{1}','{2}')".format(myip,myport,mytype)
        cur.execute(sql)
        conn.commit()
    except:
        conn.rollback()
        print('插入信息错误')
        raise
    finally:
        cur.close()
        conn.close()

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
res = requests.get('http://www.xicidaili.com/nn/5',headers=headers)
res.encoding = 'utf-8'
myhtml = res.text
# print(myhtml)
soup = BeautifulSoup(myhtml  ,'html.parser')
mylist= soup.select('#ip_list')
mytr = mylist[0].select('tr')
for item in mytr:
    mytd = item.select('td')
    if len(mytd) > 0:
        myip = mytd[1].text
        myport = mytd[2].text
        mytype = mytd[5].text
        ipstr = '{0}:{1}'.format(myip,myport)
        print(ipstr)
        try:
            mytext =''
            if mytype == 'http':
                mytext = requests.get("http://ip.chinaz.com/getip.aspx", proxies={'http':ipstr},timeout=2) #访问次网站可确定ip是否代理成功，并设置在50秒是否连接超时
                print(mytext.text)
            else:
                mytext = requests.get("https://ip.seeip.org", proxies={'https':ipstr},timeout=2) #访问次网站可确定ip是否代理成功，并设置在50秒是否连接超时
                print(mytext.text)
            if mytext.status_code != 200:
                print('代理无法使用')
            else:
                setSql(myip,myport,mytype)
                print("代理可用")
        except:
            print('连接代理错误')






