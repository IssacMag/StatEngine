import gopup as gp
import processindex
import datetime

cookie = 'BIDUPSID=FE2028866C4AF9822E6D7B2D80A7B199; PSTM=1626603529; BD_UPN=123253; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; __yjs_duid=1_1a76d44741aa3618f84618ec6304ee641626603848154; BAIDUID=750021F4DEDA4D52644CC990589125E1:FG=1; BDUSS=l2cXhJa24wbE1hfllOdGJmMWFwb0FFYTBEOFFLa3I4TkZvZ0ZTeDliRDRzQnRoSUFBQUFBJCQAAAAAAAAAAAEAAABtb4Uf0PnUr7H51L0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPgj9GD4I~RgVz; BDUSS_BFESS=l2cXhJa24wbE1hfllOdGJmMWFwb0FFYTBEOFFLa3I4TkZvZ0ZTeDliRDRzQnRoSUFBQUFBJCQAAAAAAAAAAAEAAABtb4Uf0PnUr7H51L0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPgj9GD4I~RgVz; delPer=0; BD_CK_SAM=1; PSINO=3; BD_HOME=1; H_PS_PSSID=34268_34099_34222_33848_34073_34107_34094_26350_22159; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_645EC=d304g0H8DBScVeANUNAjQKzPUTdSpu87ZLkq899Y63dh42K4H1zd4rDU7ky0W8MZRWyx; BAIDUID_BFESS=4B7A9781A328C27E9FEC2F6B6645E051:FG=1; sug=3; sugstore=0; ORIGIN=2; bdime=0; BA_HECTOR=a48k8l258g8la10g7i1gfaq200r; ab_sr=1.0.1_ODk2ZWE4MTU5NTI5ZjIyODk0MjE4YzVmYzg3MDNlMTM3MjUyMjBjYTgxODE0OTU4N2IwZDU4ZDE3YmUwNDU3M2M5YjRlNGFjOWNiNWU2NGQxN2Y2NmJhNjczNjdkNTUzYjhmZTYxNjcwZjgyMjg4YzgyMDkwOTQzNWViNDUyN2Y5YWU0NGVjZWQxYzk5OTc4YzMxY2IwNjYxMDMzZDA0YQ=='


# 全年
end_date = datetime.datetime.today() + datetime.timedelta(days=-2)
start_date = end_date + datetime.timedelta(days=-365)


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


def get_atlas_index(sightlist):
    for item in sightlist:
        item['atlas_index'] = gp.baidu_atlas_index(
            word=item['sight'],
            date=end_date,
            cookie=cookie
        )
        if item['atlas_index'] is not None:
            item['atlas_index'] = item['atlas_index'].to_dict()


def get_age_index(sightlist):
    for item in sightlist:
        item['age_index'] = gp.baidu_age_index(
            word=item['sight'],
            cookie=cookie
        )
        if item['age_index'] is not None:
            item['age_index'] = item['age_index'].to_dict()


def get_gender_index(sightlist):
    for item in sightlist:
        item['gender_index'] = gp.baidu_gender_index(
            word=item['sight'],
            cookie=cookie
        )
        if item['gender_index'] is not None:
            item['gender_index'] = item['gender_index'].to_dict()


def get_interest_index(sightlist):
    for item in sightlist:
        item['interest_index'] = gp.baidu_interest_index(
            word=item['sight'],
            cookie=cookie
        )
        if item['interest_index'] is not None:
            item['interest_index'] = item['interest_index'].to_dict()


def get_all_index(sightlist):
    get_search_index(sightlist)
    get_media_index(sightlist)
    get_news_index(sightlist)
    get_age_index(sightlist)
    get_atlas_index(sightlist)
    get_interest_index(sightlist)

    for item in sightlist:
        processindex.to_month(item)

    processindex.cal_ranking(sightlist)

