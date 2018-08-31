# 定时任务
import schedule
import time


def jop():
    print("开始执行")


schedule.every(10).seconds.do(jop) #每过十秒执行一次jop函数
#schedule.every(1).minutes.do(jop)#每过一分钟执行一次
#schedule.every().hour.do(job)#每小时执行一次
#schedule.every().day.at("17:24").do(jop)#每天的17:24执行一次
#schedule.every().monday.do(jop)#每周一现在执行一次
#schedule.every().wednesday.at("13:15").do(jop)#每周三的13:15执行一次
while True:
    schedule.run_pending()
    time.sleep(10)
