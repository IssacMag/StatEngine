from elasticsearch import Elasticsearch
import pandas


def get_list():
    es = Elasticsearch()
    body = {
        "_source": ["id", "sight", "comment"],
        "query": {
            "match_all": {}
        }
    }
    res = es.search(index="qunar", body=body)
    resultlist = res['hits']['hits']
    newlist = []

    for resultitem in resultlist:
        index = {
            'id': resultitem['_source']['id'],
            'sight': resultitem['_source']['sight'],
            'baidu_search_index': [],
            'baidu_news_index': [],
            'baidu_media_index': [],
            'age_index': [],
            'gender_index': [],
            'atlas_index': [],
            'interest_index': [],
            'comment': resultitem['_source']['comment'],
            'wordcloud_path': '',
            'rank': 0
        }
        newlist.append(index)

    return newlist


def save_list(sightlist):
    es = Elasticsearch()
    for item in sightlist:
        body = {
            'id': item['id'],
            'sight': item['sight'],
            'baidu_search_index': item['baidu_search_index'],
            'baidu_news_index': item['baidu_news_index'],
            'baidu_media_index': item['baidu_media_index'],
            'atlas_index': item['atlas_index'],
            'age_index': item['age_index'],
            'gender_index': item['gender_index'],
            'interest_index': item['interest_index'],
            'wordcloud_path': item['wordcloud_path'],
            'rank': item['rank']
        }
        res = es.index(index='qunar_stat', id=item['id'], body=body)
        print(res)

