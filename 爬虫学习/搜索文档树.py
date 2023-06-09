from bs4 import BeautifulSoup,element

with open('/Users/oohao/Library/Mobile Documents/com~apple~CloudDocs/py_work/爬虫学习/11_5.html','r',encoding='utf-8') as code:
    soup = BeautifulSoup(code,'html.parser')
    print(soup.find_all('h1'))
    print(soup.find_all('h2'))
    print(soup.find_all('p'))
    print(soup.find_all(['p','a']))
