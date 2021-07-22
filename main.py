
import esconnect
import getindex
import cloud


if __name__ == '__main__':
    sightlist = esconnect.get_list()  # 景区列表
    getindex.get_all_index(sightlist)  # 获取指数
    for item in sightlist:            # 词云
        cloud.create_cloud(item)
    esconnect.save_list(sightlist)  # 存入es

