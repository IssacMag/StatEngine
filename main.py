# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import esconnect
import getindex
import cloud


if __name__ == '__main__':
    sightlist = esconnect.get_list()  # 景区列表
    getindex.get_all_index(sightlist)  # 获取指数
    # for item in sightlist:
    #     cloud.create_cloud(item)
    esconnect.save_list(sightlist)  # 存入es

