import osmnx as ox
import matplotlib.pyplot as plt
import folium
import pandas as pd
"""
Road Network
Reference: https://taginfo.openstreetmap.org/
"""
fig, ax = plt.subplots()
place = 'Daan District, Taipei, Taiwan'
target={'highway':True}
Alldata = ox.geometries.geometries_from_place(place, tags=target)
data = Alldata[Alldata['element_type'] == 'way']
data = data.dropna(subset=['name'])

print("Got data")
road_type = data.highway.unique().tolist()
road_type.sort(key=lambda x:-len(data[data.highway == x]))
features = dict()
for rtype in road_type:
    features[rtype] = folium.FeatureGroup(rtype)

#%%

color = ['#32BEC3', '#37890B', '#810A63', '#4AD56B', '#EBE23A', '#C13085', '#CD4ED5', '#19E8A0', '#F7FED8', '#02ACF3', '#770B8C', '#A904CE', '#A31E90', '#3E2812', '#020A5E', '#F1C2E9', '#3FCF72', '#803E77']
roadcolor = dict()
for i in range(len(road_type)):
    roadcolor[road_type[i]] = color[i]
#%%
check = []
m = folium.Map(location=[25.0329694, 121.5654177],zoom_start=14)
for kind in road_type:
    try:
        for line in data[data['highway'] == kind]['geometry'].tolist():
            points = [[points[1], points[0]] for points in list(line.coords)]
            check.append(points)
            folium.vector_layers.PolyLine(points,line_weight=10 ,popup='<b>{}</b>'.format(kind), tooltip=kind ,color=roadcolor[kind]).add_to(features[kind])
        features[kind].add_to(m)
    except:
        pass
# for kind in road_type:
#     folium.Choropleth(data[data['highway'] == kind], line_weight=3, , legend_name=kind).add_to(m)
folium.LayerControl().add_to(m)
m.save("ALL.html")

