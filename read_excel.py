import pandas as pd
from io import StringIO
from xlsx2csv import Xlsx2csv
import time
import hashlib

def convert(dataframe):
    data = dataframe.to_dict(orient="records")
    return data

def read_excel(path: str) -> pd.DataFrame:
    start = time.time()
    buffer = StringIO()
    Xlsx2csv(path,outputencoding="utf-8").convert(buffer)
    buffer.seek(0)
    df = pd.read_csv(buffer)
    finish = time.time()
    data = convert(df)
    return "Donusum Suresi: {}".format(finish - start)

path = 'notlar.xlsx'


print(read_excel(path))


    