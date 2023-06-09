from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(),'html.parser')

#处理子标签和其他后代标签
# for child in bs.find('table',{'id':'giftList'}).children:
#     print(child)

#处理兄弟标签
# for sibling in bs.find('table',{'id':'giftList'}).tr.next_siblings:
#     print(sibling)

#处理父标签
print(bs.find('img',
            {'src':'../img/gifts/img1.jpg'})
    .parent.previous_sibling.get_text())


