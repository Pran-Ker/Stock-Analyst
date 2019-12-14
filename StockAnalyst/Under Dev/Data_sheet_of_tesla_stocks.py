from datetime import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

#Plot the
style.use('ggplot')

###Setting the Time Frame *IMP make sure it is recent

#start=dt(2016,1,1)
#end= dt(2016,12,31)

### the scraps yahoo (or any other similar website for stock sheets) for the desired stock
#df= web.DataReader('TSLA','yahoo',start,end)

#print(df.head(6))
#df.to_csv('tsla.csv')



### Read the built .csv file
df = pd.read_csv('tsla.csv', parse_dates=True)


### Display the Stocks Sheet
#print(df.head(10))


df.plot()
plt.show()
