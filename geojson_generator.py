import osmnx as ox
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def convert_to_geojson(place = ""):
    # Get the OpenStreetMap data for the location
    graph = ox.graph_from_place(place, network_type="all")
    # Convert the graph to a GeoDataFrame
    gdf = ox.graph_to_gdfs(graph, nodes=False, edges=True)
    # Convert the GeoDataFrame to GeoJSON
    geojson_file = gdf.to_crs(epsg=4326).to_json()
    return geojson_file

def save_geo_file(geo_file, path = ""):
    # Save the GeoJSON to a file
    with open(path, "w") as file:
        file.write(geo_file)
    logging.info("Saved.")

# Define the location you want to get OpenStreetMap data for
place = 'Kuching Division, Malaysia'
geo_file = convert_to_geojson(place)
save_geo_file(geo_file, "data/kuching_output.geojson")