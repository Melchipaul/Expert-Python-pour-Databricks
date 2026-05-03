import json
import urllib.request

json_data_source = 'https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/land_ocean/tavg/1/3/1850-2026/data.json'

with urllib.request.urlopen(json_data_source) as response:
    data = response.read().decode('utf-8')
    anomalies = json.loads(data)

for year, value in anomalies['data'].items():
    print(f"{year} ... {value['anomaly']}")
print('*' * 80)