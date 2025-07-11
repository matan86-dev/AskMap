import rasterio
import numpy as np

def compute_ndvi(image_path):
    with rasterio.open(image_path) as src:
        red = src.read(3).astype(float)
        nir = src.read(4).astype(float)
        ndvi = (nir - red) / (nir + red + 1e-6)
        mean_ndvi = np.nanmean(ndvi)
        return round(mean_ndvi, 3)
