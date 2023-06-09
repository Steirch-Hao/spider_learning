#raise_for_status()方法使用

import time
import requests
#伪造头部信息
myHeaders = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'
}
url='https://book.douban.com/subject/1255625/comments/?start={}&limit=20&status=P&sort=new_score'
for i in range(0,11):
    try:
        r=requests.get('https://book.douban.com/subject/1255625/comments/?start={}&limit=20&status=P&sort=new_score'.format(20*i),headers = myHeaders)
        r.raise_for_status()
        r.encoding='utf-8'

        path = '/Users/oohao/Library/Mobile Documents/com~apple~CloudDocs/py_work/爬虫学习/豆瓣评论爬取结果/评论第{}页.html'.format(i+1)
        with open(path,'w',encoding='utf-8') as file:
            file.write(r.text)
        time.sleep(3)   #抓取一页评论数据后，休眠3秒再抓取下一页
    except Exception as ex:
        print('第{}页采集出错，出错原因{}。'.format(i+1,ex))
    print('第{}页爬取完毕！'.format(i+1))
print('全部爬取完毕！')