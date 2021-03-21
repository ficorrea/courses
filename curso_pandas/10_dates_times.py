import pandas as pd
import datetime as dt

# Módulo Datetime review
someday = dt.date(2018, 12, 19)
someday.year
dt.datetime(2018, 12, 19, 17, 15, 39)
str(someday)
str(dt.datetime(2018, 12, 19, 17, 15, 39))

# Objeto pandas timestamp
pd.Timestamp('2018-12-19')
pd.Timestamp('2018/12/19')
pd.Timestamp('2018, 12, 19')
pd.Timestamp('19/12/2018')
# Tomar cuidado pois nestes casos o pandas pode inverter
pd.Timestamp('12-19-2018')
pd.Timestamp('4-3-2018')  # o dia com o mês
pd.Timestamp('2018-12-19 14:00:00')
pd.Timestamp('2018-12-19 06:00:00 PM')
pd.Timestamp(dt.datetime(2019, 12, 19))

# Objeto pandas DateTimeIndex
dates = ['2018-12-19', '2016-01-02', '2017-05-08']
dtIndex = pd.DatetimeIndex(dates)
values = [100, 200, 300]
pd.Series(values, dtIndex)

# Método pd.to_datetime()
pd.to_datetime('1984-12-19')
pd.to_datetime(dt.datetime(2018, 12, 19, 17, 15, 39))
pd.to_datetime(['2015-01-03', '2014-02-08', '2016', 'july 4th, 1996'])
times = pd.Series(['2015-01-03', '2014-02-08', '2016', 'july 4th, 1996'])
pd.to_datetime(times)
dates = (['2015-01-03', '2014-02-31', 'Hello', 'july 4th, 1996'])
pd.to_datetime(dates, errors='coerce')

# Método pd.date_range()
times = pd.date_range(start='2017-01-01', end='2017-01-10', freq='d')
pd.date_range(start='2017-01-01', end='2017-01-10', freq='2d')
pd.date_range(start='2017-01-01', end='2017-01-10', freq='b')
pd.date_range(start='2017-01-01', end='2017-01-10', freq='w')
pd.date_range(start='2017-01-01', end='2017-01-10',
              freq='w-wed')  # dia da semana
pd.date_range(start='2017-01-01', end='2017-01-10', freq='h')
pd.date_range(start='2017-01-01', end='2017-01-10', freq='3h')
pd.date_range(start='2017-01-01', end='2017-01-10', freq='MS') # ms minúsculo travou a máquina
pd.date_range(start='2017-01-01', end='2017-01-10', freq='a')
pd.date_range(start='2017-01-01', periods=25, freq='d')
pd.date_range(start='2017-01-01', periods=50, freq='b')
pd.date_range(start='2017-01-01', periods=25, freq='h')

# O .dt Acessor
dates = pd.date_range('2010-01-01', '2010-12-31', freq='24D')
s = pd.Series(dates)
s.dt.weekday_name
mask = s.dt.is_quarter_start
s[mask]

# Import Financial Dataset com pandas_datareader
from pandas_datareader import data
company = 'MSFT'
start = '2010-01-01'
end = '2017-12-31'
stocks = data.DataReader(name=company, data_source='morningstar', start=start, end=end)

# Alguns comandos não funcionam, pois não é o dataset do google

# Selecionando linhas do dataframe com o DateTimeIndex
stocks.loc["2017-11-27"]
stocks.iloc[300]
stocks.ix['2017-11-27']
stocks.loc['2013-10-01' : '2013-10-07']
days = pd.date_range(start='1991-04-12', end='2017-12-31', freq=pd.DateOffset(years=1))
mask = stocks.index.isin(days)
stocks[mask]

# Timestamp object attributes
someday = stocks.index[500]
stocks.insert(0, 'Day Week', stocks.index.weekday_name)

# Método .truncate()
stocks.truncate(before='2011-02-05', after='2012-08-02')

# Objetos pd.DateOffset
stocks = data.DataReader(name='GOOG', data_source='morningstar', start=dt.date(2000,1,1), end=dt.datetime.now())
stocks.index
stocks.index + pd.DateOffset(months=3)

# More fun com pd.DateOffset
stocks.index + pd.tseries.offsets.MonthEnd()
from pandas.tseries.offsets import *
stocks.index + YearEnd()

# Objeto Timedelta
timeA = pd.Timestamp('2016-03-31 04:35:16 PM')
timeB = pd.Timestamp('2016-03-20 02:15:49 AM')
timeA - timeB
pd.Timedelta(days=3, minutes=45, hours=12, weeks=8)

# Timedelta no dataset
