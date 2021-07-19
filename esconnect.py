from elasticsearch import Elasticsearch
import pandas

def get_list():
    es = Elasticsearch()
    body = {
        "_source": ["id", "sight", "desc"],
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
            'comment': resultitem['_source']['desc'],
            'wordcloud_path': ''
        }
        newlist.append(index)

    return newlist


def save_list(sightlist):
    es = Elasticsearch()
    for item in sightlist:
        body = {
            'id': item['id'],
            'sight': item['sight'],
            'baidu_search_index': item['baidu_search_index'].to_dict(),
            'baidu_news_index': item['baidu_news_index'].to_dict(),
            'baidu_media_index': item['baidu_media_index'].to_dict(),
            'wordcloud_path': item['wordcloud_path']
        }
        res = es.index(index='qunar_stat', body=body)
        print(res)
