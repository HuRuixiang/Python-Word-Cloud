#导入WordCloud库，可在命令行使用"pip install wordcloud"命令进行安装
from wordcloud import WordCloud

#读取文本
with open("新建文本文档.txt","r",encoding='UTF-8') as f:
    text = f.read()
#生成词云
wcd = WordCloud(background_color="white",height=500,width=500)
wcd.generate(text)
#转换为照片格式
img = wcd.to_image()
#显示照片
img.show()
#存储照片
img.save("wcd.png")
