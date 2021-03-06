file_line = 'file.geojson'
file_poly = 'file_poly.geojson'

import json
with open(file_line, 'r') as f:
    data = json.load(f)#讀入'file.geojson'檔到data

for feature in data['features']:
    if (feature['geometry']['type'] == 'LineString') & (len(feature['geometry']['coordinates']) >= 3):
        feature['geometry']['type'] = 'Polygon'
        feature['geometry']['coordinates'].append(feature['geometry']['coordinates'][0])

#with open(configFile, 'w+') as f:
#        f.write(json.dumps(confsDict, indent=2))
#
with open(file_poly, 'w+') as f:
    json.dump(data, f, indent=2)
