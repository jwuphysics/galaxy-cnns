import skimage.io
import pandas as pd
import time
import sys
from numpy import int64
import os

# stuff to make the status pretty.
class Printer():
    """Print things to stdout on one line dynamically"""
    def __init__(self, data):
        sys.stdout.write("\r\x1b[K" + data.__str__())
        sys.stdout.flush()


# load the data
df = pd.read_csv('./catalogs/SDSSspecgalsDR14_jwuphysics.csv')

width = 128
height = 128
pixelsize = 0.396

# total number of images
n_gals = df.shape[0]

for row in df.itertuples():
    # the 'scale' parameter is set to be 15 arcsec -> pixels
    scale = 15 / pixelsize / width
    
    url = ("http://skyserver.sdss.org/dr14/SkyserverWS/ImgCutout/getjpeg"
           "?ra={}"
           "&dec={}"
           "&scale={}"
           "&width={}"
           "&height={}".format(row.ra, row.dec, scale, width, height))
    if not os.path.isfile('images/{}.jpg'.format(row.objID)):
        try:
            img = skimage.io.imread(url)
            skimage.io.imsave('images/{}.jpg'.format(row.objID), img)
            time.sleep(0.5)
        except urllib.error.HTTPError:
            pass
    current = row.Index / n_gals * 100
    status = "{:.3f}% of {} completed.".format(current, n_gals)
    Printer(status)

    time.sleep(0.2)
