from glob import glob
import numpy as np
import os
from scipy.misc import imread, imsave
from tqdm import tqdm

PATH = os.path.abspath('..')

#
for dir_name in ['train', 'test']:
    print(f'Working on {dir_name}')
    for fname in tqdm(glob(f'{PATH}/{dir_name}/*.jpg')):
        obj_id = os.path.split(fname)[1][:-4]
        
        image = imread(fname)
        try:
            r_band = np.stack([image[:, :, 1] for _ in range(3)], axis=-1)
            imsave(f'{PATH}/{dir_name}-r/{obj_id}.jpg', r_band)
        except IndexError:
            continue
        
