import pandas as pd
import numpy as np

train_data = pd.read_csv('Data/train.csv')
train_data.columns = [x.lower() for x in train_data.columns]
