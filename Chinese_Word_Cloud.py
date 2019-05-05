#导入WordCloud库，可在命令行使用"pip install wordcloud"命令进行安装
from wordcloud import WordCloud
#需导入jieba库，可在命令行使用"pip install jieba"命令进行安装
import jieba
import numpy as np
from PIL import Image

#读取文本
with open("新建文本文档.txt","r") as f:
    text = f.read()
wt = " ".join(jieba.lcut(text))
#载入轮廓图
mask = np.array(Image.open("1.png"))
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
