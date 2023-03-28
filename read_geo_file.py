import geopandas as gpd
import matplotlib.pyplot as plt
from copy import deepcopy

gdf = gpd.read_file('data/kuching_output.geojson')
print(gdf.head())
print(gdf.info())

gdf_cop = gdf.copy()
num_nans = gdf_cop.isnull().sum(axis=1)
threshold = 5
gdf_cop_drop = gdf_cop[num_nans <= threshold]
print(gdf_cop_drop.head())

gdf.plot()
plt.title('Kuching')
plt.show()
