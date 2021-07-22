import os
from os import path
import jieba
import re
import jieba.analyse
import wordcloud
import matplotlib.pyplot as plt

exclude = {
    '岛', '的', '就', '和', '是', '在', '也', '了', '有', '比如', '的话', '像', '主要', '这里', '还是', '平方', '公里', '导游'
}


def create_cloud(sightitem):
    washed = re.sub('[^\u4e00-\u9fa5]+', ' ', sightitem['comment'])

    freq_dict = {}
    tags = jieba.analyse.extract_tags(washed, topK=40, withWeight=True)
    for tag in tags:
        freq_dict[tag[0]] = tag[1]

    wc = wordcloud.WordCloud(
        width=1000,
        height=700,
        font_path="./assets/SourceHanSansCN-Normal.ttf",
        background_color='white',
        stopwords=exclude,
        colormap=plt.get_cmap('YlGnBu'))
    wc.generate_from_frequencies(freq_dict)
    filename = sightitem['id'] + '.png'
    cloud_path = path.join('clouds', filename)
    wc.to_file(cloud_path)
    sightitem['wordcloud_path'] = cloud_path
