import requests
import pandas as pd
import geopandas as gpd
from shapely.geometry import LineString,Point
import  matplotlib.pyplot as plt
import time
import folium
City = 'NewTaipei'
url = "https://traffic.transportdata.tw/MOTC/v2/Road/Traffic/SectionShape/City/{}/".format(City)
params = { '$count':"true" ,'$format':'JSON'}
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
GeoRoad = pd.DataFrame(requests.get(url, params=params, headers=headers).json()['SectionShapes'])
url = "https://traffic.transportdata.tw/MOTC/v2/Road/Traffic/Section/City/{}/".format(City)
RoadInfo = pd.DataFrame(requests.get(url, params=params, headers=headers).json()["Sections"])
RoadInfo.set_index("SectionID", drop=True, inplace=True)
RoadInfo = RoadInfo.drop(["SectionStart", "SectionEnd"], axis=1).sort_index()
PointsName = RoadInfo["RoadSection"].tolist()
RoadInfo["Start"] = [p["Start"] for p in PointsName]
RoadInfo["End"] = [p["End"] for p in PointsName]

#%%
RoadInfo["geometry"] = [LineString([tuple([float(num) for num in loc.split(" ")]) for loc in string[string.find("(")+1:-1].split(',')]) for string in GeoRoad.sort_values("SectionID")["Geometry"].tolist()]


#%%

gdf = gpd.GeoDataFrame(RoadInfo)
gdf.crs = {'init':"epsg:4326"}
# time.sleep(10)
m = folium.Map([121.5, 25.0], zoom_start=10)
folium.Choropleth(gdf, line_weight=3, line_color='blue').add_to(m)
m.save("test.html")
