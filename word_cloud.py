# #导入WordCloud库，可在命令行使用"pip install wordcloud"命令进行安装
# from wordcloud import WordCloud

# #读取文本
# with open("yes-minister.txt","r",encoding='UTF-8') as f:
#     mytext = f.read()
# #生成词云
# wcd = WordCloud(background_color="white",height=500,width=500)
# wcd.generate(mytext)
# #转换为照片格式
# img = wcd.to_image()
# #显示照片
# img.show()
# #存储照片
# # img.save("wcd.png")

##################################################################################
#中文分词
#导入WordCloud库，可在命令行使用"pip install wordcloud"命令进行安装
from wordcloud import WordCloud
import numpy as np
from PIL import Image
#需提前安装"jieba"库，可在命令行使用"pip install jieba"命令进行安装
import jieba

#读取文本
with open("C:\\Users\\问津\\Desktop\\新建文本文档.txt","r") as f:
    text = f.read()
wt = " ".join(jieba.lcut(text))
#载入轮廓图
mask = np.array(Image.open("C:\\Users\\问津\\Desktop\\Picture\\0DSCF1236.png"))
#生成词云
wcd = WordCloud(background_color=None,height=500,width=500,font_path="fonts/msyh.ttc",
                colormap="Reds",mask=mask,mode="RGBA",repeat=True)
wcd.generate(wt)
#转换为照片格式
img = wcd.to_image()
#显示照片
img.show()
#存储照片
img.save("wcd1.png")