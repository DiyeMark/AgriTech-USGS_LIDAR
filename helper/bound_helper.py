import json
import pdal
import pandas as pd
import geopandas as gpd
from helper.file_helper import read_json, read_csv
from model.bounds import Bounds
from helper.geopandas_helper import get_gp_dep


def get_pipeline(bounds: str, polygon_str: str, region: str, filename: str):
    pipe = read_json("../data/pipeline.json")
    pipe['pipeline'][0]['filename'] = 'https://s3-us-west-2.amazonaws.com/usgs-lidar-public/' + region + "/ept.json"
    pipe['pipeline'][0]['bounds'] = bounds
    pipe['pipeline'][1]['polygon'] = polygon_str
    pipe['pipeline'][6]['out_srs'] = f'EPSG:{26915}'
    pipe['pipeline'][7]['filename'] = str('../data/laz' + "/" + str(filename + ".laz"))
    pipe['pipeline'][8]['filename'] = str('../data/tif' + "/" + str(filename + ".tif"))
    return pdal.Pipeline(json.dumps(pipe))


def check_valid_bound(bounds: Bounds, regions: list) -> bool:
    for _, row in regions.iterrows():
        cond = (row['xmin'] <= bounds.xmin) & (row['xmax'] >= bounds.xmax) & (
                row['ymin'] <= bounds.ymin) & (row['ymax'] >= bounds.ymax)
        if cond is False:
            return False

    return True


def get_dep(bounds: Bounds, polygon_str: str, region: list) -> gpd.GeoDataFrame:
    filename = region + "_" + bounds.get_bound_name()
    pl = get_pipeline(bounds.get_bound_str(),
                      polygon_str, region, filename)
    try:
        pl.execute()
        dep_data = get_gp_dep(pl.arrays)
        print(f"successfully read geodata: {filename}")
        return dep_data
    except RuntimeError as e:
        raise Exception(f"error reading geodata, error: {e}")


def get_bound_metadata(bounds: Bounds) -> pd.DataFrame:
    metadata_csv = read_csv("../data/metadata.csv")
    filtered_df = metadata_csv.loc[
        (metadata_csv['xmin'] <= bounds.xmin)
        & (metadata_csv['xmax'] >= bounds.xmax)
        & (metadata_csv['ymin'] <= bounds.ymin)
        & (metadata_csv['ymax'] >= bounds.ymax)
        ]
    return filtered_df[["filename", "region", "year"]]