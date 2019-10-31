import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.daily import *
from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key=key)

symbol = 'AAPL'

def test_daily_pull():
    data, meta_data = ts.get_daily(symbol, outputsize='full')
    assert isinstance(data, dict)
    assert isinstance(meta_data, dict)
    daily_pull(symbol)
    assert os.path.isfile('src/data/' + symbol + '.json') == True
