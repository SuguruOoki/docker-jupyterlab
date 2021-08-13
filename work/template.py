# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# !pip install git+https://github.com/MasamichiIdeue/redquery.git
# !pip install urllib3
# !pip install redash-toolbelt
# !pip install redash-dynamic-query
# !pip install git+https://github.com/ariarijp/pandash
# !python -V

# +
from redash_dynamic_query import RedashDynamicQuery
import json

from pandash import query_to_df

redash = RedashDynamicQuery(
    endpoint='', # baseURLまでで問題なし
    apikey='',
    #取得したいデータソースIDを設定
    data_source_id=1
)

#取得したいクエリIDを設定
query_id = 576

# bind = {
# "start_date":  '2021-01-01T00:00:00',
# "end_date":  '2017-12-31T23:59:59',
# }
print(query_to_df(redash, query_id))

# redashのクエリ結果を取得
# result = redash.query(query_id)
# res = result['query_result']['data']

#jsonを整形
# res_format_json = json.dumps(res, indent=4, separators=(',', ': '))
# print(res_format_json)
# -


