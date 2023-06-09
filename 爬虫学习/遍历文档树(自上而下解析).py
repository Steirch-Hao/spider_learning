###1.自上而下解析
from bs4 import  BeautifulSoup,element

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


soup=BeautifulSoup(code,'html.parser')

#1.使用contents属性输出<table>标签所有子节点列表
#print(soup.table.contents)  #输出<table>标签所有子节点     #换行符也作为子节点

#2.对children属性做循环，输出<table>标签对子标签
#for child in soup.table.children:
#    if type(child) != element.NavigableString:  #过滤标签之间对换行符
#        print(child)

#3.对descendants属性做循环，输出<table>标签的后代标签
for des in soup.table.descendants:
    if type(des) != element.NavigableString:    #过滤标签之间的换行符
        print(des)

print(1)