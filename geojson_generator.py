import osmnx as ox
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class GeoConverter:
    def __init__(self):
        pass
    
    def convert_to_geojson(self, location):
        # Get the OpenStreetMap data for the location
        if location == '' or location is None:
            logging.error("Please input a valid location!")
            return None
        else:
            try:
                graph = ox.graph_from_place(location, network_type='all')
                # Convert the graph to a GeoDataFrame
                gdf = ox.graph_to_gdfs(graph, nodes=False, edges=True)
                # Convert the GeoDataFrame to GeoJSON
                geojson_file = gdf.to_crs(epsg=4326).to_json()
                return geojson_file
            except:
                logging.error('Please check if input location is valid.')

    def save_geofile(self, geo_file, path = ''):
        if geo_file is None:
            logging.info("No geojson file was generated. Operation complete.")
        else:
            # Save the GeoJSON to a file
            path = f'data/{path}'
            with open(path, "w") as file:
                file.write(geo_file)
            logging.info("Saved.")
            
    def generate_google_maps_url(self, latitude, longitude, zoom):
        base_url = "https://www.google.com/maps/search/?api=1"
        location_string = f"{latitude},{longitude}"
        zoom_string = f"&zoom={zoom}"
        return f"{base_url}&query={location_string}{zoom_string}"

