
from datetime import datetime as dt
#import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start=dt(2016,1,1)
end= dt(2016,12,31)

df= web.DataReader('TSLA','yahoo',start,end)
print(df.head(6))
