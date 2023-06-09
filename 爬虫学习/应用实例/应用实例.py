import time,requests,jieba
from bs4 import BeautifulSoup
from wordcloud import WordCloud

#伪造头部信息
myHeaders = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'}

#函数1:爬取给定url的html文档
def getHtmlDoc(url,page):
    try:
        url = url.format(20*page)
        r = requests.get(url,timeout=30,headers = myHeaders)
        r.raise_for_status()
        r.encoding='utf-8'
        return r.text
    except Exception as ex:
        print('第{}页采集出错，出错原因：{}。'.format(page,ex))
        return ''                                     ######这里的return是什么意思？？？##########

#函数2:获取给定html文档中第评论内容，返回评论列表
def getComment(html):
    comment = []    #该列表用于存储当前页面第所有评论
    soup = BeautifulSoup(html,'html.parser')
    div = soup.find('div',id='comments')

    #获取<div>标签内部的所有列表项标签<li>,再获取后代标签<p>、<span>
    for li in div.find_all('li',{'class':'comment-item'}):
        p = li.find('p',{'class':'comment-item'})
        text = p.span.string
        comment.append(text)
    return comment

#函数3:根据给定评论文件，利用jieba库分词后生成词云文件
def createWordCloud(fileName):
    with open(fileName,'r',encoding='utf-8') as file:
        text = file.read()
        ls_word = jieba.lcut(text)  #利用jieba库对所有评论进行分词
        all_words = ','.join(ls_word)   #所有词语以逗号连接成一个长字符串
        wcloud = WordCloud(font_path = r'/Users/oohao/Library/Mobile Documents/com~apple~CloudDocs/py_work/爬虫学习/simhei.ttf',
                    width=1000,height=800,
                    background_color='white',
                    max_words=200,
                    margin=2)
        wcloud.generate(all_words)
        #生成词云图片文件，主文件名同文本文件名
        fileCloud = fileName.split('.')[0]+'.png'
        wcloud.to_file(fileCloud)

#一下为主程序
url = 'https://book.douban.com/subject/1255625/?start={}&limit=20&status=P&sort=new_score'
all_comment = []    #存储全部评论的列表

for p in range(1,201):
    html = getHtmlDoc(url,p)   #循环爬取前200页html文档
    page_comment = getComment(html) #从html文档中抽取评论内容
    all_comment.extend(page_comment)    #每页的评论列表添加到总列表中
time.sleep(2)     #每爬取一页暂停2s
print('第{}页处理完成。'.format(p))   

print('网页采集结束，开始写入文件、生成词云。')
#评论列表全部写入文件
fileName = '/Users/oohao/Library/Mobile Documents/com~apple~CloudDocs/py_work/爬虫学习/天龙八部评论.txt'
with open(fileName,'w',encoding='utf-8') as file:
    file.writelines(all_comment)

#根据评论文件生成词云
createWordCloud(fileName)
print('词云生成结束。')


