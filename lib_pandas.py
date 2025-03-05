import pandas as pd
import numpy as np
data = [10, 20, np.nan, 40, 50, 60, np.nan, 80, 90, 100]
index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
s = pd.Series(data, index=index)
print("\nFill NaN with 0:\n", s.fillna(0))
print("Drop NaN values:\n", s.dropna())
print("\nSum:", s.sum())
print("Mean:", s.mean())
print("Median:", s.median())
print("Standard Deviation:", s.std())
print("Minimum value:", s.min())
print("Maximum value:", s.max())
print("\nSquared values using apply:\n", s.apply(lambda x: x**2))
print("Rank of values:\n", s.rank())
print("\nAggregated stats:\n", s.agg(['sum', 'min', 'max', 'mean']))

