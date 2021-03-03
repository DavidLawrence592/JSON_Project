import json


with open("US_fires_9_1.json") as data_file:
    data = json.load(data_file)


brights, lons, lats = [], [], []


for fr in data:
    bright = fr["brightness"]
    lon = fr["longitude"]
    lat = fr["latitude"]
    if bright >= 450:
        brights.append(bright)
        lons.append(lon)
        lats.append(lat)


print(brights[:10])
print(lons[:10])
print(lats[:10])


from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "marker": {
            "size": [bright % 5 for bright in brights],
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
