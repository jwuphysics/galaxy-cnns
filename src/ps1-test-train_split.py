"""A quick train/test split of the test and training data (images)"""

import numpy as np
import os
import pandas as pd
import shutil
from tqdm import tqdm

# path variable
PATH = os.path.abspath('..')

# read in training data subset
df_train = pd.read_csv(f'{PATH}/catalogs/train-oh_p50.csv', index_col=0)

# copy training images to ps1-train directory
legit_trn_idx = []
for objid in tqdm(df_train.index, total=len(df_train)):
    try:
        shutil.copyfile(f'{PATH}/ps1/{objid}.jpg', f'{PATH}/ps1-train/{objid}.jpg')
        legit_trn_idx.append(objid)
    except FileNotFoundError:
        continue
df_train = df_train.iloc[legit_trn_idx].copy()
df_train.to_csv(f'{PATH}/catalogs/ps1-train.csv', index_col=0)


# repeat for test data
df_test = pd.read_csv(f'{PATH}/catalogs/test-oh_p50.csv', index_col=0)

legit_test_idx = []
for objid in tqdm(df_test.index, total=len(df_test)):
    try:
        shutil.copyfile(f'{PATH}/ps1/{objid}.jpg', f'{PATH}/ps1-test/{objid}.jpg')
        legit_test_idx.append(objid)
    except FileNotFoundError:
        continue
df_test = df_test.iloc[legit_test_idx].copy()
df_test.to_csv(f'{PATH}/catalogs/ps1-test.csv', index_col=0)
