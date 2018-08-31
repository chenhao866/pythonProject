import sys
import requests


strUrl='http://gsyh.hncd.cn/gsyh/module/attach/DownloadFile.aspx?attachment_id=E67AABE2DDF0403C21278A02ACE624AF&name=2011%e5%b9%b4%e7%ab%8b%e9%a1%b9%e6%8a%a5%e5%91%8a.doc'
luJing = "C://Users//Administrator//Downloads//wenjian.doc"#下载路径
'''下载文件'''
r = requests.get(strUrl,stream=True,verify = False)
total_size = int(r.headers['Content-Length'])
temp_size = 0
with open(luJing, "wb") as f:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            temp_size += len(chunk)
            f.write(chunk)
            f.flush()
            done = int(50 * temp_size / total_size)
            sys.stdout.write("\r[%s%s] %d%%" % ('█' * done, ' ' * (50 - done), 100 * temp_size / total_size))
            sys.stdout.flush()
print()
