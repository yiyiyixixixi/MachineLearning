"""
Python code analysis of titanic data set.
"""

import warnings

import pandas as pd
import seaborn as sns

warnings.filterwarnings('ignore')

sns.set(style='white', context='notebook', palette='deep')

train = pd.read_csv("../dataset/train.csv")
test = pd.read_csv("../dataset/test.csv")

print(train.info())
print(test.info())

print(train.head(10))
