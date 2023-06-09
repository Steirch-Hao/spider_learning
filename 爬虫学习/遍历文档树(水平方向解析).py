from bs4 import BeautifulSoup,element

code='''<html><head>
    <title>网页标题</title></head>
    <body><h2>金庸群侠传</h2>
    <table width='400px' border='1'>
    <tr><th>书名</th> <th>人物</th> <th>年份</th></tr>
    <tr><td>《射雕英雄传》</td> <td>郭靖</td> <td>1959年</td></tr>
    <tr><td>《倚天屠龙记》</td> <td>张无忌</td> <td>1961年</td></tr>
    <tr><td>《笑傲江湖》</td> <td>令狐冲</td> <td>1967年</td></tr>
    <tr><td>《鹿鼎记》</td> <td>韦小宝</td> <td>1972年</td></tr>
    </table></body></html>
'''
soup = BeautifulSoup(code,'html.parser')

# for child in soup.table.tr.next_siblings:   #获取第一行向后的兄弟标签
#     if type(child) != element.NavigableString:  #过滤标签之间的换行
#         print(child)

#soup.table.tr获取的已经是表格第一行，也就是标题行，它不能把自己看作兄弟标签，所以next_siblings属性获取到的就是后面所有的数据行

with open('/Users/oohao/Library/Mobile Documents/com~apple~CloudDocs/py_work/爬虫学习/11_5.html','r',encoding='utf-8') as code:
    soup = BeautifulSoup(code,'html.parser')
    print(soup.find_all(attrs={'class':'css1'}))