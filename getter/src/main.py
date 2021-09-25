import pymongo
import pprint
import datetime
import time
import pandas as pd
import numpy as np
myclient = pymongo.MongoClient("mongodb://localhost:27017/", username='root', password="root")

mydb = myclient["history"]
mycol = mydb["transfer_cycle"]

d = datetime.datetime.strptime("2021-09-13T10:53:53.000Z", "%Y-%m-%dT%H:%M:%S.000Z")
d1 = datetime.datetime.strptime("2021-09-13T11:00:53.000Z", "%Y-%m-%dT%H:%M:%S.000Z")
c = 0

while True:
    c += 1
    d = datetime.datetime.now()
    mydict = {
        "timestamp": d,
        "count": c
    }
    print(c)

    mycol.insert_one(mydict)
    # val = mydb["transfer_cycle"].find_one(sort=[("date", -1)])
    time.sleep(1)
    # val = mydb["transfer_cycle"].find(sort=[("date", -1)])
    # pd1 = pd.DataFrame(list(val))
    # val = mydb["transfer_cycle"]\
    #     .find({"timestamp": {'$gte': datetime.datetime(2021, 9, 25, 00, 46, 00)}}, sort=[("timestamp", -1)])
    # data = pd.DataFrame(val)
    # print(data.memory_usage())

    val = mydb["transfer_cycle"]\
        .find({"timestamp": {'$gte': datetime.datetime(2021, 9, 25, 00, 46, 00)}}, sort=[("timestamp", -1)])
    data = pd.DataFrame(list(val))
    print(len(data))
    print(data)
    print(np.arange(len(data)) // 5)
    data = data.groupby(np.arange(len(data)) // 5).mean()
    print(data)
    # print(pd1)
    # print(val["count"])

