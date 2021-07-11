#导入jieba库
import jieba
#导入wordcloud库，这个有难度，需要好好说一下
#一般来说直接用pip install wordcloud是安装不成功的
#登录这个网址：https://www.lfd.uci.edu/~gohlke/pythonlibs/，然后选择wordcloud-1.8.1-cp39-cp39-win_amd64.whl这个文件，下载到本地
#然后拷贝到D:\Users\Administrator\AppData\Local\Programs\Python\Python39\Scripts这个目录来，Scripts之前的路径代表python的安装路径和python的版本
#所以我们在刚才下载时是选择cp39，也就是与python39相对应
import wordcloud
#from scipy.misc import imread
#在我的机器上scipy和imread不兼容，所以选择了imageio，也可以实现同样的功能
from imageio import imread
#str部分的代码测试了jiba生成词云的功能，也就是分词的功能
str='师傅，他为何说禅机已到,\
     佛祖点化世人讲究机缘,\
     禅机一过缘即灭矣,\
     而禅机未到虽点亦不中\
     我愿化身石桥又是何意'

print(str)
words=jieba.lcut(str)
print(words)

#通过open函数读取了一个文本文件
f=open('七一讲话.txt','r',encoding='utf-8')
#打印文件格式
print('文件的编码格式'+f.encoding)
# 读取文件
txt=f.read()
#打印文件
print(txt)
#关闭文件，良好习惯
f.close()

#使用精确模式对文本进行分词
#使用结巴库把文本文件拆分成一个个的词组
words=jieba.lcut(txt)
#打印分词后的结果
print(words)


#使用join()方法，将分词生成的字符串以空格进行分割。因为在生成词云时，字符串之间需为空格
txt=' '.join(words)
print(txt)
#用imread来读取一个图片
pic=imread(r'tree.jpg')

#实例词云对象，设置词云字体 背影颜色 词云形状
#这里simkai.ttf是一个楷体的字库文件，需要提前放到python程序相同的目录下
w=wordcloud.WordCloud(font_path=r'simkai.ttf',background_color='white',mask=pic)

#生成词云
w.generate(txt)

#生成图片
w.to_file(r'七一讲话.png')