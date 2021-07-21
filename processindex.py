import pandas as pd
import numpy as np


# 按月整理
def to_month(item):
    if item['baidu_search_index'] is not None:
        series = \
            item['baidu_search_index'].fillna(0).groupby(pd.Grouper(freq='M'))[item['sight']].sum()
        item['baidu_search_index'] = series.to_frame()[item['sight']].tolist()
    if item['baidu_news_index'] is not None:
        series = \
            item['baidu_news_index'].fillna(0).groupby(pd.Grouper(freq='M'))[item['sight']].sum()
        item['baidu_news_index'] = series.to_frame()[item['sight']].tolist()
    if item['baidu_media_index'] is not None:
        series = \
            item['baidu_media_index'].fillna(0).groupby(pd.Grouper(freq='M'))[item['sight']].sum()
        item['baidu_media_index'] = series.to_frame()[item['sight']].tolist()


# “高于xx%的景点”
def cal_ranking(sight_list):
    total_sight = len(sight_list)  # 景点总数
    index_list = []
    for item in sight_list:
        if len(item['baidu_search_index']):
            index_list.append(item['baidu_search_index'][-1])  # 取出最近一个月的index用于排序
        else:
            index_list.append(0)
    rankings = [sorted(index_list).index(x)+1 for x in index_list]  # 排序列表 从1开始
    for item in sight_list:
        index = sight_list.index(item)
        item['rank'] = 1 - rankings[index]/total_sight
