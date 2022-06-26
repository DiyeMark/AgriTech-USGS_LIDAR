from shapely.geometry import Polygon
from helper.bound_helper import check_valid_bound, get_dep, get_bound_metadata
from helper.file_helper import read_csv
from helper.geopandas_helper import get_bound_from_polygon, get_gp_dep


class FetchLidar:
    def __init__(self):
        self._metadata = read_csv("../data/metadata.csv")

    def fetch_lidar_data(self, polygon: Polygon, regions: list) -> list:
        bound, polygon_str = get_bound_from_polygon(polygon)
        print('bound, polygon_str')
        print(bound, polygon_str)
        if len(regions) == 0:
            regions = get_bound_metadata(bound)
        else:
            regions = self._metadata[self._metadata['filename'].isin(regions)]
            if check_valid_bound(bound, regions) is False:
                raise Exception("The boundary is not within the region provided")

        list_geo_data = []
        for index, row in regions.iterrows():
            try:
                data = get_dep(bound, polygon_str, row['filename'])
                if (data is not None):
                    list_geo_data.append({'year': row['year'],
                                          'region': row['region'],
                                          'geo_data': data,
                                          })
            except RuntimeError as e:
                raise Exception(
                    f"error featching geo data for {row['filename']}, error: {e}")
        return list_geo_data
