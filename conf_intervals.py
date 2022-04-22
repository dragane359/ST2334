import scipy.stats as stats
from math import *

def known_mean_variance(mean, alpha, n, sd): # alpha/2
    left = mean + stats.norm.ppf(alpha)*(sd/sqrt(n))
    right = mean + stats.norm.ppf(1 - alpha)*(sd/sqrt(n))
    return (left, right)

def unknown_mean_variance_lessthan30(mean, alpha, df, n, samplesd): #df -1 first, alpha/2
    left = mean + stats.t(df).ppf(alpha)*(samplesd/sqrt(n))
    right = mean + stats.t(df).ppf(1 - alpha)*(samplesd/sqrt(n))
    return (left, right)

def unknown_mean_variance_morethan30(mean, alpha, n, samplesd): #df -1 first, alpha/2
    left = mean + stats.norm.ppf(alpha)*(samplesd/sqrt(n))
    right = mean + stats.norm.ppf(1 - alpha)*(samplesd/sqrt(n))
    return (left, right)

def diffbtw_known_mean_variance(mean1, mean2, alpha, n1, n2, sd1, sd2): #df -1 first, alpha/2
    left = mean1 - mean2 + stats.norm.ppf(alpha)*(sqrt(((sd1**2)/n1) + ((sd2**2)/n2)))
    right = mean1 - mean2 + stats.norm.ppf(1 - alpha)*(sqrt(((sd1**2)/n1) + ((sd2**2)/n2)))
    return (left, right)

def diffbtw_unknown_mean_variance_morethan30(mean1, mean2, alpha, n1, n2, sampsd1, sampsd2): #df -1 first, alpha/2
    left = mean1 - mean2 + stats.norm.ppf(alpha)*(sqrt(((sampsd1**2)/n1) + ((sampsd2**2)/n2)))
    right = mean1 - mean2 + stats.norm.ppf(1 - alpha)*(sqrt(((sampsd1**2)/n1) + ((sampsd2**2)/n2)))
    return (left, right)

def diffbtw_unknown_butequal_variance_lessthan30(mean1, mean2, alpha, n1, n2, sampsd1, sampsd2): #df -1 first, alpha/2
    sqp = ((n1 - 1) * sampsd1**2 + (n2 - 1) * sampsd2**2) / (n1 + n2 - 2)
    left = mean1 - mean2 + stats.t(n1 + n2 - 2).ppf(alpha) * sqrt(sqp) * sqrt(1/n1 + 1/n2)
    right = mean1 - mean2 + stats.t(n1 + n2 - 2).ppf(1 - alpha) * sqrt(sqp) * sqrt(1/n1 + 1/n2)
    return (left, right)

def diffbtw_unknown_butequal_variance_morethan30(mean1, mean2, alpha, n1, n2, sampsd1, sampsd2): #df -1 first, alpha/2
    sqp = ((n1 - 1) * sampsd1**2 + (n2 - 1) * sampsd2**2) / (n1 + n2 - 2)
    left = mean1 - mean2 + stats.norm.ppf(alpha) * sqrt(sqp) * sqrt(1/n1 + 1/n2)
    right = mean1 - mean2 + stats.norm.ppf(1 - alpha) * sqrt(sqp) * sqrt(1/n1 + 1/n2)
    return (left, right)

def diffbtw_unknown_paired_lessthan30(dbar, n, alpha, sampsd): #df -1 first, alpha/2
    left = dbar + stats.t(n - 1).ppf(alpha)*(sampsd / sqrt(n))
    right = dbar + stats.t(n - 1).ppf(1 - alpha)*(sampsd / sqrt(n))
    return (left, right)

def diffbtw_unknown_paired_morethan30(dbar, n, alpha, sampsd): #df -1 first, alpha/2
    left = dbar + stats.norm.ppf(alpha)*(sampsd / sqrt(n))
    right = dbar + stats.norm.ppf(1 - alpha)*(sampsd / sqrt(n))
    return (left, right)

def confint_sdsquared_mean_unknown(n, alpha, sampsd): #df -1 first, alpha/2
    left = (n -1)*sampsd**2 / (stats.chi2(n - 1).ppf(1 - alpha))
    right = (n -1)*sampsd**2 / (stats.chi2(n - 1).ppf(alpha))
    return (left, right)

def confint_sdsquared_mean_known(n, alpha, sampsd): #df -1 first, alpha/2
    left = sampsd / (stats.chi2(n).ppf(1 - alpha))
    right = sampsd / (stats.chi2(n).ppf(alpha))
    return (left, right)

def confint_ratioof2sd_mean_known(alpha, n1, n2, sampsd1, sampsd2): #df -1 first, alpha/2, take not is sd not sd**2
    left = sqrt((sampsd1**2/sampsd2**2) * (1/(stats.f(n1 - 1, n2 - 1).ppf(1 - alpha))))
    right = sqrt((sampsd1**2/sampsd2**2) * ((stats.f(n2 - 1, n1 - 1).ppf(1 - alpha))))
    return (left, right)