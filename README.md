# Kepler maps

![portada](https://miro.medium.com/max/1440/1*bB0OTIKP51yoKgKG6Bd9zg.gif)

`Kepler.gl` is an open-source solution for geospatial data visualization and exploration. Kepler was developed by Uber to make it easier for users of all levels to design meaningful maps that also look good. The tool can handle large amounts of data and has a friendly, intuitive interface that allows users to build effective maps in an instant.

# Install Kepler in Jupyter Notebook

To install `kepler` in jupyter notebook visit the [oficial page](https://docs.kepler.gl/docs/keplergl-jupyter)

**Prerequisites**  
- Python >= 2  
- ipywidgets >= 7.0.0

## Libraries

- [kepler](https://kepler.gl/)  
- [pandas](https://pandas.pydata.org/docs/)
- [geopandas](https://geopandas.org/)

# Main parameters
## Add_data `add_data()`
Inputs: 

- `data` required CSV, GeoJSON or DataFrame. 
- `name` required data entry.
`name` of the dataset dataId property of each `layer`, `filter` and interaction
    ```python
    # DataFrame
    df = pd.read_csv('hex-data.csv')
    map_1.add_data(data=df, name='data_1')

    # CSV
    with open('csv-data.csv', 'r') as f:
        csvData = f.read()
    map_1.add_data(data=csvData, name='data_2')

    # GeoJSON as string
    with open('sf_zip_geo.json', 'r') as f:
        geojson = f.read()

    map_1.add_data(data=geojson, name='geojson')
    ```

## Save and load config `.config`

- Map configuration
    ```python
    map_1.config
    ## {u'config': {u'mapState': {u'bearing': 2.6192893401015205,
    #  u'dragRotate': True,
    #   u'isSplit': False,
    #   u'latitude': 37.76209132041332,
    #   u'longitude': -122.42590232651203,
    ```

- Config the map
    ```python
    config = {
        'version': 'v1',
        'config': {
            'mapState': {
                'latitude': 37.76209132041332,
                'longitude': -122.42590232651203,
                'zoom': 12.32053899007826
            }
            ...
        }
    },
    map_1.add_data(data=df, name='data_1')
    map_1.config = config
    ```
- Map config
    ```python
    map_1 = KeplerGl(height=400, data={'data_1': my_df}, config=config)
    ```
- Config %run
    ```python
    # Save map_1 config to a file
    with open('hex_config.py', 'w') as f:
    f.write('config = {}'.format(map_1.config))

    # load the config
    %run hex_config.py
    ```


## Save the map `.save_to_html()`

Input
- `data`: optional A data dictionary {"name": data}, if not provided, will use current map data
- `config`: optional map config dictionary, if not provided, will use current map config
- `file_name`: optional the html file name, default is keplergl_map.html
- `read_only`: optional if read_only is True, hide side panel to disable map customization
You can export your current map as an interactive html file.
    ```python
    # this will save current map
    map_1.save_to_html(file_name='first_map.html')

    # this will save map with provided data and config
    map_1.save_to_html(data={'data_1': df}, config=config, file_name='first_map.html')

    # this will save map with the interaction panel disabled
    map_1.save_to_html(file_name='first_map.html' read_only=True)
    ```

## Data used in this repo

**1 -NYC Taxi Trips**

The yellow and green taxi trip records include fields capturing pick-up and drop-off dates/times, pick-up and drop-off locations, trip distances, itemized fares, rate types, payment types, and driver-reported passenger counts. Data is downloaded from NYC Taxi and Limousine Commission (TLC) website. Data source: [TLC](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

**2- San Francisco street tree map**

This dataset contains a list of dpw maintained street trees including planting date, species and location. Data source: [DataSF](https://data.sfgov.org/City-Infrastructure/Street-Tree-List/tkzw-k3nq/data).

**3- Block number Vancuver**

**4- Graffiti number Vancuver**

**5- Mean Average temperature**

**6- NYPD shoots**

**7- Earthsquares** 

**8- UK moves**

**9- San Francisco countour**




## Further Materials

https://kepler.gl/  
https://leadr-msu.github.io/kepler-gl/    
https://github.com/heshan0131/kepler.gl  
https://towardsdatascience.com4d-data-visualization-with-kepler-gl-b6bd6dd90451  