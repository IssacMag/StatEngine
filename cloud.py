import os
from os import path
import jieba
import re
import jieba.analyse
import wordcloud


def create_cloud(sightitem):
    washed = re.sub('[^\u4e00-\u9fa5]+', ' ', sightitem['comment'])

    freq_dict = {}
    tags = jieba.analyse.extract_tags(washed, topK=40, withWeight=True)
    for tag in tags:
        freq_dict[tag[0]] = tag[1]

    # 先安装思源黑体
    wc = wordcloud.WordCloud(width=1000, font_path="./assets/SourceHanSansCN-Normal.ttf", height=700)
    wc.generate_from_frequencies(freq_dict)
    filename = sightitem['id'] + '.png'
    cloud_path = path.join(os.getcwd(), 'clouds', filename)
    wc.to_file(cloud_path)
    sightitem['wordcloud_path'] = cloud_path
