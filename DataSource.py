import requests
import pandas as pd

City = 'Taipei'
url = "https://traffic.transportdata.tw/MOTC/v2/Road/Traffic/SectionShape/City/{}/".format(City)
params = { '$count':"true" ,'$format':'JSON'}
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
GeoRoad = pd.DataFrame(requests.get(url, params=params, headers=headers).json()['SectionShapes'])
url = "https://traffic.transportdata.tw/MOTC/v2/Road/Traffic/Section/City/{}/".format(City)
RoadInfo = pd.DataFrame(requests.get(url, params=params, headers=headers).json()["Sections"])
RoadInfo.set_index("SectionID", drop=True, inplace=True)
RoadInfo = RoadInfo.drop(["SectionStart", "SectionEnd"], axis=1).sort_index()
RoadInfo["Geometry"] = GeoRoad.sort_values("SectionID")["Geometry"].tolist()
PointsName = RoadInfo["RoadSection"].tolist()
RoadInfo["Start"] = [p["Start"] for p in PointsName]
RoadInfo["End"] = [p["End"] for p in PointsName]
