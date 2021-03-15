import requests
import pandas as pd


lat = 25.0376993
lng = 121.5390153
url = "https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?point={}%2C{}".format(lat,lng)
params = {
    # 'point':"25.0376993%2C121.5390153",
    'unit':'KMPH',
    'key': 'CRi8cJ8JZnHcBp7iSFxWYIB9txTKyOGh'
    }

res = requests.get(url, params=params).json()
