from shapely.geometry import Polygon
from scripts.fetch_lidar import FetchLidar


class Lidar:
    def __init__(self):
        self._fetch_lidar = FetchLidar()

    def fetch_lidar(self, polygon: Polygon, regions=[]):
        return self._fetch_lidar.fetch_lidar_data(polygon, regions)
