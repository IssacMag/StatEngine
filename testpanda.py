import gopup as gp
import datetime
import pandas as pd
import numpy as np

cookie = 'BIDUPSID=FE2028866C4AF9822E6D7B2D80A7B199; PSTM=1626603529; BD_UPN=123253; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; __yjs_duid=1_1a76d44741aa3618f84618ec6304ee641626603848154; BAIDUID=750021F4DEDA4D52644CC990589125E1:FG=1; BDUSS=l2cXhJa24wbE1hfllOdGJmMWFwb0FFYTBEOFFLa3I4TkZvZ0ZTeDliRDRzQnRoSUFBQUFBJCQAAAAAAAAAAAEAAABtb4Uf0PnUr7H51L0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPgj9GD4I~RgVz; BDUSS_BFESS=l2cXhJa24wbE1hfllOdGJmMWFwb0FFYTBEOFFLa3I4TkZvZ0ZTeDliRDRzQnRoSUFBQUFBJCQAAAAAAAAAAAEAAABtb4Uf0PnUr7H51L0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPgj9GD4I~RgVz; delPer=0; BD_CK_SAM=1; PSINO=3; BD_HOME=1; H_PS_PSSID=34268_34099_34222_33848_34073_34107_34094_26350_22159; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_645EC=d304g0H8DBScVeANUNAjQKzPUTdSpu87ZLkq899Y63dh42K4H1zd4rDU7ky0W8MZRWyx; BAIDUID_BFESS=4B7A9781A328C27E9FEC2F6B6645E051:FG=1; sug=3; sugstore=0; ORIGIN=2; bdime=0; BA_HECTOR=a48k8l258g8la10g7i1gfaq200r; ab_sr=1.0.1_ODk2ZWE4MTU5NTI5ZjIyODk0MjE4YzVmYzg3MDNlMTM3MjUyMjBjYTgxODE0OTU4N2IwZDU4ZDE3YmUwNDU3M2M5YjRlNGFjOWNiNWU2NGQxN2Y2NmJhNjczNjdkNTUzYjhmZTYxNjcwZjgyMjg4YzgyMDkwOTQzNWViNDUyN2Y5YWU0NGVjZWQxYzk5OTc4YzMxY2IwNjYxMDMzZDA0YQ=='

# end_date = datetime.datetime.today() + datetime.timedelta()
# start_date = end_date + datetime.timedelta(days=-365)

start_date = '2021-05-01'
end_date = '2021-06-30'

df = gp.baidu_search_index(word='西湖', start_date=start_date, end_date=end_date, cookie=cookie)

# df2 = gp.baidu_search_index(word='武当山', start_date=start_date, end_date=end_date, cookie=cookie)

# 见了鬼了 怎么没有数据的
# print(df.groupby([df.index.year, df.index.month], dropna=True, sort=False, axis=0).mean())

# ndf = df.fillna(0).groupby(pd.Grouper(freq='M'))['西湖'].sum()


print(df)

