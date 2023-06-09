from urllib.request import urlopen
from bs4 import BeautifulSoup
#异常处理
from urllib.error import HTTPError
from urllib.error import URLError

#html = urlopen('http://pythonscraping.com/pages/page1.html')
#可能出现的异常⬆️
'''
try:
    html = urlopen('http://pythonscraping.com/pages/page1.html')
#·网页在服务器上不存在（或者获取页面的时候出现错误）
    #程序会返回HTTP错误。可能是‘404 Page Not Found’或者‘500 Internal Server Error’
    #·解决方案⬇️
except HTTPError as e:
    print(e)
    #返回空值，中断程序，或者执行另一个方案

#·服务器不存在
    #如果服务器不存在（就是说链接http://pythonscraping.com 打不开，或者是URL链接写错了），urlopen会抛出一个URLError异常。
    #这意味着获取不到服务器，并且由于远程服务器负责返回HTTP状态代码，所以不能抛出HTTPError异常，
    #而且还应该捕捉到更严重的URLErrory异常
    #·解决方案⬇️
except URLError as e:
    print('The server could not be found!')

else:
    #程序继续。注意：如果已经在上面异常捕捉那一段代码里返回或中断（break），
    #那么就不需要使用else语句里，这段代码也不会执行
    bs = BeautifulSoup(html,'html.parser')
    print(bs.h1)
    print(bs.nonExistengTag.someTag)
'''

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(),'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title
    
title = getTitle('http://pythonscraping.com/pages/page1.html')
if title == None:
    print('Title could not be found')
else:
    print(title)