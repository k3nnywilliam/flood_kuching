from geojson_generator import GeoConverter
import argparse
parser = argparse.ArgumentParser()

if __name__  == "__main__":
    #place = 'Kuching Division, Malaysia'
    parser.add_argument("--location", type=str, required=True)
    parser.add_argument("--out", type=str)
    args = parser.parse_args()
    place = args.location
    output_file = args.out
    geoconvert = GeoConverter()
    geofile = geoconvert.convert_to_geojson(place)
    #data/kuching_output.geojson
    geoconvert.save_geofile(geo_file = geofile, path = output_file)