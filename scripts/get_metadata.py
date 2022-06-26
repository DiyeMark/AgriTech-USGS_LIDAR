import json
import re

import pandas as pd
import urllib3

from helper.file_helper import read_txt, write_csv


class GetMetadata:
    def __init__(self):
        self.http = urllib3.PoolManager()

    def get_metadata(self):
        regex = '20[0-9][0-9]+'
        df = pd.DataFrame(columns=['filename', 'region', 'year', 'xmin', 'xmax', 'ymin', 'ymax', 'points'])

        filenames = read_txt('../data/filename.txt')
        for filename in filenames:
            response = self.http.request('GET', 'https://s3-us-west-2.amazonaws.com/usgs-lidar-public/'
                                         + filename + 'ept.json')

            match = re.search(regex, filename)

            if response.status == 200:
                response_json = json.loads(response.data)
                df = df.append({
                    'filename': filename.replace('/', ''),
                    'region': filename[:match.start() - 1] if match else filename,
                    'year': filename[match.start():match.end()] if match else None,
                    'xmin': response_json['bounds'][0],
                    'xmax': response_json['bounds'][3],
                    'ymin': response_json['bounds'][1],
                    'ymax': response_json['bounds'][4],
                    'points': response_json['points']}, ignore_index=True)
                print(df)
            else:
                pass

        write_csv(df, '../data/metadata.csv')


if __name__ == "__main__":
    get_metadata = GetMetadata()
    get_metadata.get_metadata()
