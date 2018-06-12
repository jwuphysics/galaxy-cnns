"""A quick 80/20 split of the test and training data (images + catalogs)"""

import numpy as np
import os
import pandas as pd
import shutil
from tqdm import tqdm

# path variable
PATH = os.path.abspath('..')

# grab label data
label_csv = f'{PATH}/catalogs/SDSSspecgalsDR14_boada.csv'
df = pd.read_csv(label_csv, index_col='objID')

# decide which columns to use
cols = ['oh_p2p5', 'oh_p16', 'oh_p50', 'oh_p84', 'oh_p97p5']
df = df[cols].copy()

# do random split
split_idxs = np.arange(len(df))
np.random.shuffle(split_idxs)

train_idxs = split_idxs[:-25000]
test_idxs  = split_idxs[-25000:]

# copy files to train-small dir, also make copy of data frame which only has 
# valid images
valid_train_idxs = []
for objid, idx in tqdm(zip(df.iloc[train_idxs].index, train_idxs), total=len(train_idxs)):
    try:
        shutil.copyfile(f'{PATH}/images/{objid}.jpg', f'{PATH}/train/{objid}.jpg')
        valid_train_idxs.append(idx)
    except FileNotFoundError:
        continue

# save mini-dataframe
df_train = df.iloc[valid_train_idxs].copy()
df_train.to_csv(f'{PATH}/catalogs/train-metaldist.csv')

# do the same thing, except for test-small dataset
valid_test_idxs = []
for objid, idx in tqdm(zip(df.iloc[test_idxs].index, test_idxs), total=len(test_idxs)):
    try:
        shutil.copyfile(f'{PATH}/images/{objid}.jpg', f'{PATH}/test/{objid}.jpg')
        valid_test_idxs.append(idx)
    except FileNotFoundError:
        continue

# save mini-dataframe *and sort by index*
df_test = df.iloc[valid_test_idxs].copy()
df_test.sort_index(inplace=True)
df_test.to_csv(f'{PATH}/catalogs/test-metaldist.csv')


