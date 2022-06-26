# AgriTech - USGS LIDAR
10 Academy Batch 5 - Weekly Challenge: Week 7

**Table of content**
  - [Overview](#overview)
  - [Requirements](#requirements)
  - [Install](#install)
  - [Data](#data)
  - [Notebooks](#notebooks)
  - [Scripts](#scripts)
  - [Test](#test)

## Overview
A Python module that will allow users to quickly handle, convert, sample, and visualize the geographical data from 3DEP.

## Requirements 
- PDAL
- Geopandas

## Install
```
git clone https://github.com/DiyeMark/AgriTech-USGS_LIDAR
cd AgriTech-USGS_LIDAR
pip install -r requirements.txt
```

## Data 
- Access to the lidar point cloud data from the 3DEP repository is made possible through the USGS 3D Elevation Program (3DEP). Users can work with enormous amounts of lidar point cloud data without having to download them to local computers thanks to 3DEP's adoption of cloud computing and storage.
- The point cloud data is available via AWS in an open format called EPT. A straightforward and adaptable octree-based storage format for point cloud data is called Entwine Point Tile (EPT). Binary point data and JSON metadata are both included in the structure of an EPT dataset. To interpret the contents of an EPT dataset, the JSON file is essential metadata.

## Notebooks
- the folder where example notebooks are stored

## Scripts
- all scripts files of the python package

## Test
- the folder containing unit tests for components in the scripts

## Quickstart Guide

```python
from lidar import Lidar
from visualization import Visualization
from shapely.geometry import Polygon

# initialize lidar
lidar = Lidar()

# build polygon
MINX, MINY, MAXX, MAXY = [-93.756155, 41.918015, -93.747334, 41.921429]
polygon = Polygon(((MINX, MINY), (MINX, MAXY), (MAXX, MAXY), (MAXX, MINY), (MINX, MINY)))

# geopandas dataframe of the polygon region
geo_df = lidar.fetch_lidar(polygon, ["IA_FullState"])

# geodata of the polygon region
df = geo_df[0]['geo_data']

# initialize visualization
vis = Visualization()

# heatmap
vis.plot_heatmap(df, column='elevation', title='IA_FullState Heatmap')

# 3d plot
vis.plot_3d_map(df)
```
