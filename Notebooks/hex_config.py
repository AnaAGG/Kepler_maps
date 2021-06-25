config = {'version': 'v1', 'config': {'visState': {'filters': [{'dataId': ['crimes'], 'id': '7xs8kg41e', 'name': ['PERP_RACE'], 'type': 'multiSelect', 'value': ['BLACK'], 'enlarged': False, 'plotType': 'histogram', 'animationWindow': 'free', 'yAxis': None}], 'layers': [{'id': 'evlwyhl', 'type': 'hexagon', 'config': {'dataId': 'crimes', 'label': 'Point', 'color': [18, 147, 154], 'columns': {'lat': 'Latitude', 'lng': 'Longitude'}, 'isVisible': True, 'visConfig': {'opacity': 0.8, 'worldUnitSize': 0.3, 'resolution': 8, 'colorRange': {'name': 'Global Warming', 'type': 'sequential', 'category': 'Uber', 'colors': ['#5A1846', '#900C3F', '#C70039', '#E3611C', '#F1920E', '#FFC300']}, 'coverage': 1, 'sizeRange': [0, 500], 'percentile': [0, 100], 'elevationPercentile': [0, 100], 'elevationScale': 5, 'colorAggregation': 'average', 'sizeAggregation': 'count', 'enable3d': True}, 'hidden': False, 'textLabel': [{'field': None, 'color': [255, 255, 255], 'size': 18, 'offset': [0, 0], 'anchor': 'start', 'alignment': 'center'}]}, 'visualChannels': {'colorField': {'name': 'PRECINCT', 'type': 'integer'}, 'colorScale': 'quantize', 'sizeField': None, 'sizeScale': 'linear'}}, {'id': '7l7j0xp', 'type': 'geojson', 'config': {'dataId': 'crimes', 'label': 'crimes', 'color': [221, 178, 124], 'columns': {'geojson': 'New Georeferenced Column'}, 'isVisible': False, 'visConfig': {'opacity': 0.8, 'strokeOpacity': 0.8, 'thickness': 0.5, 'strokeColor': None, 'colorRange': {'name': 'Global Warming', 'type': 'sequential', 'category': 'Uber', 'colors': ['#5A1846', '#900C3F', '#C70039', '#E3611C', '#F1920E', '#FFC300']}, 'strokeColorRange': {'name': 'Global Warming', 'type': 'sequential', 'category': 'Uber', 'colors': ['#5A1846', '#900C3F', '#C70039', '#E3611C', '#F1920E', '#FFC300']}, 'radius': 10, 'sizeRange': [0, 10], 'radiusRange': [0, 50], 'heightRange': [0, 500], 'elevationScale': 5, 'stroked': False, 'filled': True, 'enable3d': False, 'wireframe': False}, 'hidden': False, 'textLabel': [{'field': None, 'color': [255, 255, 255], 'size': 18, 'offset': [0, 0], 'anchor': 'start', 'alignment': 'center'}]}, 'visualChannels': {'colorField': None, 'colorScale': 'quantile', 'sizeField': None, 'sizeScale': 'linear', 'strokeColorField': None, 'strokeColorScale': 'quantile', 'heightField': None, 'heightScale': 'linear', 'radiusField': None, 'radiusScale': 'linear'}}, {'id': 'zwl83n', 'type': 'icon', 'config': {'dataId': 'crimes', 'label': 'icon', 'color': [136, 87, 44], 'columns': {'lat': 'Latitude', 'lng': 'Longitude', 'icon': 'icon'}, 'isVisible': False, 'visConfig': {'radius': 10, 'fixedRadius': False, 'opacity': 0.8, 'colorRange': {'name': 'Global Warming', 'type': 'sequential', 'category': 'Uber', 'colors': ['#5A1846', '#900C3F', '#C70039', '#E3611C', '#F1920E', '#FFC300']}, 'radiusRange': [0, 50]}, 'hidden': False, 'textLabel': [{'field': None, 'color': [255, 255, 255], 'size': 18, 'offset': [0, 0], 'anchor': 'start', 'alignment': 'center'}]}, 'visualChannels': {'colorField': None, 'colorScale': 'quantile', 'sizeField': None, 'sizeScale': 'linear'}}], 'interactionConfig': {'tooltip': {'fieldsToShow': {'crimes': [{'name': 'Unnamed: 0', 'format': None}, {'name': 'INCIDENT_KEY', 'format': None}, {'name': 'OCCUR_DATE', 'format': None}, {'name': 'OCCUR_TIME', 'format': None}, {'name': 'BORO', 'format': None}, {'name': 'PERP_SEX', 'format': None}]}, 'compareMode': False, 'compareType': 'absolute', 'enabled': False}, 'brush': {'size': 10, 'enabled': False}, 'geocoder': {'enabled': False}, 'coordinate': {'enabled': False}}, 'layerBlending': 'normal', 'splitMaps': [], 'animationConfig': {'currentTime': None, 'speed': 1}}, 'mapState': {'bearing': 24, 'dragRotate': True, 'latitude': 40.67054216546428, 'longitude': -74.00606246174895, 'pitch': 50, 'zoom': 10.372785288694343, 'isSplit': False}, 'mapStyle': {'styleType': 'dark', 'topLayerGroups': {}, 'visibleLayerGroups': {'label': True, 'road': True, 'border': False, 'building': True, 'water': True, 'land': True, '3d building': False}, 'threeDBuildingColor': [9.665468314072013, 17.18305478057247, 31.1442867897876], 'mapStyles': {}}}}