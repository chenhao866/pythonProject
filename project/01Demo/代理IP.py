#代理IP
import requests
import random

#爬取网站是http就用http代理，不然就用https代理
proxies =["219.141.153.35:80", "219.141.153.3:80","219.141.153.38:80"]
url = random.choice(proxies) #从列表中随机生成一个ip
print(url)
try:
    mytext = requests.get("http://ip.chinaz.com/getip.aspx", proxies={'http':url},timeout=2) #访问次网站可确定ip是否代理成功，并设置在50秒是否连接超时
    print(mytext.text)
    if mytext.status_code != 200:
        print('代理无法使用')
    else:
        print("代理可用")
except:
    print('连接代理错误')
