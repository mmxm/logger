import pymongo
import pprint
import datetime
import time
import pandas as pd
import numpy as np
myclient = pymongo.MongoClient("mongodb://localhost:27017/", username='root', password="root")

mydb = myclient["history"]
mycol = mydb["transfer_cycle"]

val = mydb["transfer_cycle"] \
    .find({"timestamp": {'$gte': datetime.datetime(2021, 9, 25, 00, 46, 00)}}, sort=[("timestamp", -1)])
data = pd.DataFrame(list(val))
#data.floor('D')
print(len(data))
print(data)
#data = data.set_index('timestamp')
#print(data.index.get_level_values('timestamp').floor('D'))
data_min = data.groupby(pd.Grouper(key='timestamp',freq='D')).min()
data_max = data.groupby(pd.Grouper(key='timestamp',freq='D')).max()
data = data_max['count'] - data_min['count']
#data.rename({'0':'new column name'})
print(data)

#print(data.set_index('timestamp').groupby(['count']).resample('D').sum().reset_index())
#print(np.arange(len(data)) // 5)
#data = data.groupby(np.arange(len(data)) // 5).mean()
#print(data)