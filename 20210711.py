import jieba
import wordcloud
#from scipy.misc import imread
#from scipy.misc import imread
from imageio import imread
str='师傅，他为何说禅机已到,\
     佛祖点化世人讲究机缘,\
     禅机一过缘即灭矣,\
     而禅机未到虽点亦不中\
     我愿化身石桥又是何意'

print(str)

words=jieba.lcut(str)

print(words)
f=open('七一讲话.txt','r',encoding='utf-8')
print('文件的编码格式'+f.encoding)
# 读取文件
txt=f.read()
print(txt)
#关闭文件，良好习惯
f.close()

#使用精确模式对文本进行分词
#使用结巴库把西游拆分成一个个的词组
words=jieba.lcut(txt)
print(words)

#通过键值对的形式存储词语及其出现的次数
#大括号表示python的字典类型对应,
#键值对key:value1,类似java的map对象和list
#counts={}

#使用join()方法，将分词生成的字符串以空格进行分割。因为在生成词云时，字符串之间需为空罕
txt=' '.join(words)
print(txt)
#pic=
pic=imread(r'tree.jpg')

#实例词云对象，设置词云字体 背影颜色 词云形状
w=wordcloud.WordCloud(font_path=r'simkai.ttf',background_color='white',mask=pic)

#生成词云
w.generate(txt)

#生成图片
w.to_file(r'七一讲话.png')