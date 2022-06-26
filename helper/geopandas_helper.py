import geopandas as gpd
import numpy as np
from model.bounds import Bounds
from shapely.geometry import Point, Polygon


def get_bound_from_polygon(polygon: Polygon) -> tuple:
    polygon_df = gpd.GeoDataFrame([polygon], columns=['geometry'])
    polygon_df.set_crs(epsg=4326, inplace=True)
    polygon_df['geometry'] = polygon_df['geometry'].to_crs(epsg=3857)
    xmin, ymin, xmax, ymax = polygon_df['geometry'][0].bounds
    bound = Bounds(xmin, xmax, ymin, ymax)
    x_cord, y_cord = polygon_df['geometry'][0].exterior.coords.xy
    polygon_str = get_polygon_str(x_cord, y_cord)
    return bound, polygon_str


def get_polygon_str(x_cord, y_cord) -> str:
    polygon_str = 'POLYGON(('
    for x, y in zip(list(x_cord), list(y_cord)):
        polygon_str += f'{x} {y}, '
    polygon_str = polygon_str[:-2]
    polygon_str += '))'
    return polygon_str


def get_gp_dep(array_data: np.ndarray) -> gpd.GeoDataFrame:
    for i in array_data:
        geometry_points = [Point(x, y) for x, y in zip(i["X"], i["Y"])]
        elevations = np.array(i["Z"])

        df = gpd.GeoDataFrame(columns=["elevation", "geometry"])
        df['elevation'] = elevations
        df['geometry'] = geometry_points
        df = df.set_geometry("geometry")
        df.set_crs(epsg=26915, inplace=True)
        return df
