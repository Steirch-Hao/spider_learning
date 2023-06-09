from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(),'html.parser')

nameList = bs.findAll('span',{'class':'green'})     #bs.find_all(tagName,tagAttributes)
for name in nameList:
    print(name.get_text())
        #.get_text()会清除你正在处理的HTML文档中的所有标签，然后返回一个只包含文字的unicode字符串
        #通常在准备打印、存储和操作最终数据时，应该最后才使用.get_text()。一般情况，应尽可能保留HTML文档的标签结构

nameList = bs.find_all(text='the prince')
print(len(nameList))





