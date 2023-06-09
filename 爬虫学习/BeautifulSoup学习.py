import requests
import bs4
r= requests.get('http://baidu.com')
r.encoding = 'utf-8'

#新建BeautifulSoup对象，赋值给soup变量
soup = bs4.BeautifulSoup(r.text,'html.parser')


with open('/Users/oohao/Library/Mobile Documents/com~apple~CloudDocs/py_work/爬虫学习/11_5.html','r',encoding='utf-8') as code:
    '''
    #1.Tag对象
    soup = bs4.BeautifulSoup(code,'html.parser')
    print(soup.p)   #输出标签对象
    print(type(soup.p))     #输出对象类型
    print(soup.p.name)  #输出标签类型

    print(soup.p.attrs) #输出标签属性字典
    print(soup.p['name'])   #输出标签name属性
    print(soup.p['class'])  #输出标签class属性
    '''

    #3.NavigableString对象
    soup=bs4.BeautifulSoup(code,'html.parser')
    print(soup.h1.string)   #输出h1标签包含的字符串
    print(soup.p.string)    #输出p标签包含的字符串  
    print(type(soup.p.string))
