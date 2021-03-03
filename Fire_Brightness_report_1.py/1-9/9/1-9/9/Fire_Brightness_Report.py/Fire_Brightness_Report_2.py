import json


with open("US_fires_9_14.json") as data_file2:
    data2 = json.load(data_file2)


brights2, lons2, lats2 = [], [], []


for fr in data2:
    bright2 = fr["brightness"]
    lon2 = fr["longitude"]
    lat2 = fr["latitude"]
    if bright2 >= 450:
        brights2.append(bright2)
        lons2.append(lon2)
        lats2.append(lat2)

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [
    {
        "type": "scattergeo",
        "lon": lons2,
        "lat": lats2,
        "marker": {
            "size": [bright % 5 for bright in brights2],
            "color": brights2,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Brightness"},
        },
    }
]

my_layout = Layout(title="Fire Bightness Report 9/14-9/21")

fig = {"data": data, "layout": my_layout}


offline.plot(fig, filename="firebrightnessreport2.html")
