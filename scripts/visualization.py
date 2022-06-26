import numpy as np
import matplotlib.pyplot as plt
import rasterio
from rasterio.plot import show, show_hist


class Visualization:
    def __init__(self):
        pass

    def plot_raster(self, rast_data, title='', figsize=(10, 10)):
        plt.figure(figsize=figsize)
        im1 = plt.imshow(np.log1p(rast_data), )  # vmin=0, vmax=2.1)

        plt.title("{}".format(title), fontdict={'fontsize': 20})
        plt.axis('off')
        plt.colorbar(im1, fraction=0.03)

    def plot_raster_from_file(self, file):
        src = rasterio.open(file)
        fig, (axrgb, axhist) = plt.subplots(1, 2, figsize=(14, 7))
        show(src, cmap='Greys_r', contour=True, ax=axrgb)
        show_hist(src, bins=50, histtype='stepfilled',
                  lw=0.0, stacked=False, alpha=0.3, ax=axhist)
        plt.show()

    def plot_heatmap(self, df, column, title):
        fig, ax = plt.subplots(1, 1, figsize=(12, 10))
        fig.patch.set_alpha(0)
        plt.grid('on', zorder=0)
        df.plot(column=column, ax=ax, legend=True, cmap="terrain")
        plt.title(title)
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.show()

    def plot_3d_map(self, data):
        fig, ax = plt.subplots(1, 1, figsize=(12, 10))
        fig.set_size_inches(18.5, 10.5, forward=True)
        ax = plt.axes(projection='3d')
        x = data.geometry.x
        y = data.geometry.y
        z = data.elevation
        points = np.vstack((x, y, z)).transpose()
        ax.scatter(points[:, 0], points[:, 1], points[:, 2], s=0.01)
        ax.set_xlabel('Longitude')
        ax.set_ylabel('Latitude')
        plt.show()
