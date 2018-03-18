import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader as web

style.use('ggplot') # styple of plot

"""start = dt.datetime(2000,1,1)
end = dt.datetime(2016,12,31)

df = web.DataReader('NASDAQ:TSLA', 'google', start, end) # a ticker a symbol for the company's stock
print('Google Finance (note: has been deprecated due to stability issues)')
print(df.head())"""

"""print('Robinhood (note: can get only a years worth of data)')
start1 = dt.datetime(2017,3,10)
end1 = dt.datetime(2018,2,1)
df2 = web.DataReader('TSLA', 'robinhood', start1, end1)
df2.to_csv('TSLA.csv')"""

df = pd.read_csv('TSLA.csv', parse_dates=True, index_col=1)

# rolling average for 100 day periods
#df['100ma'] = df['close_price'].rolling(window=100, min_periods=0).mean()
# df['50ma'] = df['close_price'].rolling(window=50, min_periods=0).mean()
# df.dropna(inplace=True) # this removes rows with a NaN value

"""
Resampling is redistributing your data (such as changing collecing data every minute to every hour)
"""
df_ohlc = df[close_price].resample('10D').ohlc()
df_vol = df['volume'].resample('10D').sum()
print(df_ohlc)
print(df_vol)

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

"""ax1.plot(df.index, df['close_price'], label='close_price')
ax1.plot(df.index, df['100ma'], label="100ma")
#ax1.plot(df.index, df['50ma'], label='50ma')
ax2.bar(df.index, df['volume'])
plt.legend(loc='upper right')
plt.show()"""