#web开发
from flask import Flask,url_for,redirect,render_template
import myconfig

app = Flask(__name__)
app.config.from_object(myconfig)  #添加自定义配置文件

@app.route('/') # 修饰器，确定访问http://127.0.0.1:5000/时执行的这个函数
def hello():
    '''
    strurl = url_for('setData',mysum = 123)  #url反转。即在知道函数名称的情况下，得到和这个函数对应的URL。如果没有形参的话直接写函数名
    print('url反转值：{0}'.format(strurl))

    return redirect(strurl) #跳转到别的页面。strurl是一个URL地址 如：/app/123/
    '''

    mycontext = {
        'myisoff':1,
        'myvalue1':'我是值1',
        'myvalue2':'我是值2'
    }
    return render_template('home.html',**mycontext)  #在当前文件夹创建templates文件夹。执行当前函数跳转到home.html,并可以以传值,传的是字典，这样就可以传多个值


@app.route('/app/<mysum>/') # 修饰器，确定访问http://127.0.0.1:5000/app/123时执行的这个函数,123可自定义参数
def setData(mysum):
   return '超链接传参：{0}'.format(mysum)

@app.route('/long/')
def longPage():
    return '重定向页面'


if __name__ == '__main__':
    app.run()
