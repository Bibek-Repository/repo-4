import numpy as np
from scipy.stats import ttest_ind
from scipy.stats import kstest
from scipy.stats import describe
from scipy.stats import skew, kurtosis

v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)
res = ttest_ind(v1, v2)
print(res)

# for returning only p-value,
res = ttest_ind(v1,v2).pvalue
print(res)

# KS-Test
v = np.random.normal(size=100)
res = kstest(v, 'norm')
print(res)

# Statistical Description
v = np.random.normal(size = 100)
res = describe(v)
print(res)

# skewness and Kurtosis
v = np.random.normal(size = 100)
print(skew(v))
print(kurtosis(v))  # the values are nearly equal to 0, because the distribution is nearlyy normal.

