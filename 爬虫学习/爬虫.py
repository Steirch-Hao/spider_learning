import requests
'''
#伪造头部信息
myHeaders = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'
}
url = 'https://zhihu.com'
r = requests.get(url,headers = myHeaders)
r.encoding='utf-8'

print(r.status_code)
print(r.text)
'''


#encoding属性使用
r = requests.get('http://www.baidu.com')
r.encoding = 'utf-8'    #方法一：直接转换Response对象的编码格式
print(r.text)

'''
r = requests.get('http://www.baidu.com')
print(r.content.decode('utf-8'))    #方法二：对二进制内容以utf-8格式解码
'''


'''
#content属性的使用
r = requests.get('http://www.baidu.com/img/bd_logo1.png')
path = "/Users/oohao/Library/Mobile Documents/com~apple~CloudDocs/py_work/爬虫学习/baidu.png"    #下载文件的存放路径 及 新文件名
with open(path,'wb') as file:     #以二进制+写模式新建文件
    file.write(r.content)
'''
