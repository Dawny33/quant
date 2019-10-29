# Get vals from config file
import configparser
import json
import os
import sys

config = configparser.ConfigParser()
config.read('config.ini')
alphav_path = config['alphav_params']['path']
key = config['api']['key']

# Add dev version of alpha_vantage to sys path
sys.path.append(alphav_path)
import alpha_vantage.alphavantage as alpha_vantage

# Initial experiments with alpha_vantage time series module
from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key=key)
"""
# Get json object with the intraday data and another with  the call's metadata
data, meta_data = ts.get_daily('GOOGL')
print(data)
"""

def daily_pull(symbol: str):
    """
    Pulls the bulk daily data and stores them as json files in local folder
    Usage: daily_pull('GOOGL')

    Params:
        symbol: The name of the ticker symbol for which the data is needed 
    """
    data, meta_data = ts.get_daily(symbol, outputsize='full')
    if not os.path.exists('data/'):
        os.makedirs('data/')
    with open('data/' + symbol + '.json', 'w') as fp:
        json.dump(data, fp)
