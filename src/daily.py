# Get vals from config file
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
alphav_path = config['alphav_params']['path']
key = config['api']['key']

# Add dev version of alpha_vantage to sys path
import sys
sys.path.append(alphav_path)
import alpha_vantage.alphavantage as alpha_vantage

# Initial experiments with alpha_vantage time series module
from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key=key)
# Get json object with the intraday data and another with  the call's metadata
data, meta_data = ts.get_intraday('GOOGL')
print(data)