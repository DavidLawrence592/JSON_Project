import json


with open("US_fires_9_1.json") as data_file:
    data = json.load(data_file)
with open("US_fires_9_14.json") as data_file2:
    data2 = json.load(data_file2)

brights, lons, lats = [], [], []
brights2, lons2, lats2 = [], [], []

for fr in data:
    bright = fr["brightness"]
    lon = fr["longitude"]
    lat = fr["latitude"]
    brights.append(bright)
    lons.append(lon)
    lats.append(lat)

for fr in data2:
    bright2 = fr["brightness"]
    lon2 = fr["longitude"]
    lat2 = fr["latitude"]
    brights2.append(bright2)
    lons2.append(lon2)
    lats2.append(lat2)
"""
print(brights[:10])
print(lons[:10])
print(lats[:10])

print(brights2[:10])
print(lons2[:10])
print(lats2[:10])
"""

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "marker": {
            "size": [450 * bright for bright in brights],
            "color": brights,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Brightness"},
        },
    }
]

my_layout = Layout(title="Fire Bightness Report 9/1 - 9/13")

fig = {"data": data, "layout": my_layout}


offline.plot(fig, filename="firebrightnessreport.html")
