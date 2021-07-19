import pandas as pd
import numpy as np


# 按月整理
def to_month(item):
    if item['baidu_search_index'] is not None:
        series = \
            item['baidu_search_index'].fillna(0).groupby(pd.Grouper(freq='M'))[item['sight']].sum()
        item['baidu_search_index'] = series.to_frame()
    if item['baidu_news_index'] is not None:
        series = \
            item['baidu_news_index'].fillna(0).groupby(pd.Grouper(freq='M'))[item['sight']].sum()
        item['baidu_news_index'] = series.to_frame()
    if item['baidu_media_index'] is not None:
        series = \
            item['baidu_media_index'].fillna(0).groupby(pd.Grouper(freq='M'))[item['sight']].sum()
        item['baidu_media_index'] = series.to_frame()



def cal_ranking(sight_list):
    index_list = []
    for item in sight_list:
        index_list.append(item['baidu_search_index'])

    df = pd.concat(index_list, axis=1)
    print(df.index)
