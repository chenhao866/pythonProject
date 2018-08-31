#爬虫
import requests
import json # 解析json数据
from bs4 import BeautifulSoup #解析html标签
res = requests.get('http://a.heiyan.com/ajax/chapter/content/2448113?callback=jQuery183009375593461432796_1530973514210&_=1530973514863')
res.encoding = 'utf-8'
mystr = res.text.lstrip('jQuery183009375593461432796_1530973514210(').rstrip(')') #将返回的数据截取成json字符串
print(mystr)
mystr = mystr.replace('<p>',' ') #替换字符串
mystr = mystr.replace('</p>',' ')
mystr = mystr.replace('\\r',' ')  # 字符传中不能包含\r
jd = json.loads(mystr) #将json字符串转成python字典
print(jd)
print(jd['chapter']['htmlContent'])

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


