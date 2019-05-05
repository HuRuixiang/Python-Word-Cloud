# 观看指南
## 这是用Python写的制作词云的Demo，享与诸君，多多指教。
### Python制作词云的一般步骤
#### 1、导入相关库
    #用于生成词云
    from wordcloud import WordCloud
    #用于读取背景图
    import numpy as np
    #用于载入词云背景图
    from PIL import Image
    #用于载入jieba词库进行中文分词
    import jieba

#### 2、读取文本内容，存入一个变量text
    with open("新建文本文档.txt","r") as f:
        text = f.read()

#### 3、使用jieba库中的jieba.lcut()库进行中文分词处理，将结果返回为一个列表wt（英文文本跳过此步）
    wt = " ".join(jieba.lcut(text))

#### 4、载入背景图
    mask = np.array(Image.open("1.png"))

#### 5、在背景图(mask)上生成词云
    #注意中文文本需要导入字体包(font_path)，否则生成的词云无法显示汉字，会呈现为彩色矩形方框
    wcd = WordCloud(background_color=None,height=500,width=500,font_path="fonts/msyh.ttc",
                colormap="Reds",mask=mask,mode="RGBA",repeat=True)
    wcd.generate(wt)
    
#### 6、将词云转换为图片格式
    img = wcd.to_image()
    
#### 7、显示/存储图片
    #显示图片
    img = wcd.to_image()
    #存储图片
    img.save("wcd.png")

