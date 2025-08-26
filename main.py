import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point
# --- 1. Synthetic Data Generation ---
# Generate synthetic data for store locations, competitor proximity, and customer density
np.random.seed(42)  # for reproducibility
num_stores = 50
store_data = {
    'StoreID': range(1, num_stores + 1),
    'Latitude': np.random.uniform(37, 38, num_stores),
    'Longitude': np.random.uniform(-122, -121, num_stores),
    'CompetitorProximity': np.random.randint(1, 11, num_stores), # Distance to nearest competitor (1-10)
    'CustomerDensity': np.random.randint(50, 500, num_stores) # Customers per square km
}
df_stores = pd.DataFrame(store_data)
# Create shapely points for geospatial analysis
df_stores['geometry'] = df_stores.apply(lambda row: Point(row['Longitude'], row['Latitude']), axis=1)
gdf_stores = gpd.GeoDataFrame(df_stores, geometry='geometry', crs="EPSG:4326")
# --- 2. Analysis ---
# Calculate predicted sales uplift (simplified example)
df_stores['PredictedSalesUplift'] = (df_stores['CustomerDensity'] / df_stores['CompetitorProximity']) * 10
# Identify potential new store locations (simplified example -  high customer density, low competitor proximity)
potential_locations = df_stores[(df_stores['CustomerDensity'] > 300) & (df_stores['CompetitorProximity'] < 3)]
# --- 3. Visualization ---
# Visualize store locations and competitor proximity
plt.figure(figsize=(10, 6))
gdf_stores.plot(column='CompetitorProximity', cmap='viridis', legend=True, markersize=50, alpha=0.7, ax=plt.gca())
plt.title('Store Locations and Competitor Proximity')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('store_locations.png')
print("Plot saved to store_locations.png")
# Visualize predicted sales uplift
plt.figure(figsize=(10, 6))
plt.scatter(df_stores['CompetitorProximity'], df_stores['PredictedSalesUplift'])
plt.xlabel('Competitor Proximity')
plt.ylabel('Predicted Sales Uplift')
plt.title('Predicted Sales Uplift vs. Competitor Proximity')
plt.savefig('sales_uplift.png')
print("Plot saved to sales_uplift.png")
#Visualize potential new store locations
plt.figure(figsize=(10,6))
gdf_stores.plot(column='PredictedSalesUplift', cmap='plasma', legend=True, markersize=50, alpha=0.7, ax=plt.gca())
potential_locations.plot(ax=plt.gca(), color='red', markersize=100, label='Potential Locations')
plt.title('Potential New Store Locations')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend()
plt.savefig('potential_locations.png')
print("Plot saved to potential_locations.png")