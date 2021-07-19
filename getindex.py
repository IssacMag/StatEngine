import gopup as gp
import processindex

cookie = 'BIDUPSID=FA901BE6B2DD46D7D328EC474B7DF697; PSTM=1626013967; BAIDUID=FA901BE6B2DD46D7D22A253E69A07EBA:FG=1; __yjs_duid=1_5dc8e5712cb09e0df8cce11131a521901626017262992; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; CHKFORREG=2304b6f3770991539bc70192215195ed; bdindexid=rcep02k5ehcpopubepivmh9kl1; H_PS_PSSID=34269_33801_34222_31254_34004_34092_34094_26350_34218; delPer=0; PSINO=3; BA_HECTOR=2h212l8580802la43p1gf2ta50q; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1626332156,1626335483,1626431636,1626437959; BDUSS=dtWE14V3FLcmYzUFBwY1JUREtxYkFyaHJCeVBrQkl1MzhBVkVQVDB6VmFCaGxoSUFBQUFBJCQAAAAAAAAAAAEAAABd0SI~yfHTobvD07AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFp58WBaefFgOF; BDUSS_BFESS=dtWE14V3FLcmYzUFBwY1JUREtxYkFyaHJCeVBrQkl1MzhBVkVQVDB6VmFCaGxoSUFBQUFBJCQAAAAAAAAAAAEAAABd0SI~yfHTobvD07AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFp58WBaefFgOF; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1626437983; ab_sr=1.0.1_OGU3YjY3MzdlMTYwMmY1MDEwNWNhMWVlNjM1Mjk1MTU0NmNjNjAxY2Y3NGZiNDVmNDljZDAwNWFjOTc2OTA1MTkzNmFjYjY3NDllZjFkMjgyZDI5NzQzNjJkZDNjNjcxZWU3YzFjNGJhMTIwOTljMjk2ZDcxN2YxZDMzM2ZiZTgyNWQ4NjYxYmVkNzQ2MDAzNDg5MTMyYzJmYTAyYjNiNw==; __yjs_st=2_ZGU1ZWJiZjBhNThiODAxZWNmNjRiMzk3NGM1Y2JlNzk1NjQ3NzA3NTQ5M2QzYjU4ZTAyMDdmYWYyNTM2YWI4MzdhMmY5YmM4MDA0MGE3OGZhZmJkMDQ0MDFjNGIwYTgyYjEyMzVmNDE1NDE2MDgxZTk2ZWZlNmRjZjIzMGEzMjFlYjg1ODIxZjYxMTZiNjViOTg0OTk1ZDc5YjBiNjU0ZDk2NTZkOWNjNWM3ZGQ4YjdiN2Y4NDliYjZlNzMyYjA2Mjg2MzRlOGNlNDhmY2IxYjhhNmNhNDczMGE1OWRkMTczZmMwM2NjNDcwYjQ5YzdhYTlkNzMyNmEzZTFjYWM1Ml83XzkxOWE3MWE5; RT="z=1&dm=baidu.com&si=pqt4mqpoxxp&ss=kr6b60hh&sl=8&tt=404&bcn=https://fclog.baidu.com/log/weirwood?type=perf"'

start_date = '2021-07-10'
end_date = '2021-07-15'

# 全年
# end_date = datetime.datetime.today() + datetime.timedelta()
# start_date = end_date + datetime.timedelta(days=-365)


def get_search_index(sightlist):
    for item in sightlist:
        item['baidu_search_index'] = gp.baidu_search_index(
            word=item['sight'],
            start_date=start_date,
            end_date=end_date,
            cookie=cookie)


def get_news_index(sightlist):
    for item in sightlist:
        item['baidu_news_index'] = gp.baidu_info_index(
            word=item['sight'],
            start_date=start_date,
            end_date=end_date,
            cookie=cookie)


def get_media_index(sightlist):
    for item in sightlist:
        item['baidu_media_index'] = gp.baidu_media_index(
            word=item['sight'],
            start_date=start_date,
            end_date=end_date,
            cookie=cookie)


def get_all_index(sightlist):
    get_search_index(sightlist)
    # get_media_index(sightlist)
    # get_news_index(sightlist)
    for item in sightlist:
        processindex.to_month(item)
    processindex.cal_ranking(sightlist)

