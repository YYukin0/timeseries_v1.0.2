import requests
import numpy as np
import pandas as pd
from pathlib import Path
import talib
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

params = {
    'access_key' : 'be5c78f5649dcce4e510fac1d872fe42',
    'symbols' : 'AAPL',
    'date_from' : '2021-07-29',
    'date_to' : '2023-08-08',
    'limit' : 1000
}

api_result = requests.get('https://api.marketstack.com/v1/eod', params)

data = api_result.json()


df = pd.DataFrame(data["data"])

print(df)



df.to_csv('raw_data.csv', index=False)

# df.DataFrame.to_csv
# two_dimensional_array = []
# for record in data:
#     row = [record["date"],record["open"], record["high"], record["low"], record["close"], record["volume"], record["adj_high"],
#     record["adj_high"], record["adj_low"], record["adj_close"]
#            ]
#     two_dimensional_array.append(row)



