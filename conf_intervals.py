import scipy.stats as stats
from math import *

def known_mean_variance_2_sided(mean, alpha, n, variance):
    left = mean + stats.norm.ppf(alpha)*(variance/sqrt(n))
    right = mean + stats.norm.ppf(1 - alpha)*(variance/sqrt(n))
    return (left, right)

