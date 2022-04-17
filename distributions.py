import scipy.stats as stats
# normal dist
stats.norm.ppf(0.05)
stats.norm.ppf(0.95) # inverse standard norm
stats.norm.cdf(stats.norm.ppf(0.95)) = 0.95 # find cdf probability

# t dist
stats.t(df).ppf(0.05) # use degrees of freedom based on statistic
stats.t(20).ppf(0.05) = -1.7247182429207863
stats.t(20).cdf(-1.7247182429207863) = 0.05 # find cdf probability

# chisq dist
stats.chi2(9).ppf(0.95) # df based on statistic, since chisq is >, use 1-alpha
stats.chi2(9).cdf(stats.chi2(9).ppf(0.95)) = 0.95 # find cdf probability, since chisq is >, use 1-alpha
1 - stats.chi2(df).cdf(n) # to find p(x2 > n)

# f dist
stats.f(n1 - 1, n2 - 1).ppf(0.95)
stats.f(10,8).ppf(0.95) # df based on statistic, since F is >, use 1-alpha
stats.f(10,8).cdf(stats.f(10,8).ppf(0.95)) = 0.95 # find cdf probability, since F is >, use 1-alpha

# binom dist
stats.binom(n,p).pmf(x)
stats.binom(n,p).cdf(x) # less than or equal to

# negative binom dist
stats.nbinom(no of successes, p).pmf(no of failures b4 success) 
stats.nbinom(4,0.55).pmf(2) # 4 successes in 6 
stats.nbinom(no of successes, p).cdf(max - number of successes) - stats.nbinom(no of successes,p).cdf(min - number of successes) # cdf for a range (e.g. btw 4 and 7) when u have a max number of tries
stats.nbinom(4,.55).cdf(3)-stats.nbinom(4,.55).cdf(-1) # example from slides (3 - 4 = -1)

# geom dist
stats.nbinom(1, 0.05).pmf(x - 1)
stats.nbinom(1, 0.05).pmf(x - 1) # cummulative

# poisson dist
stats.poisson(lambda).pmf(x)
stats.poisson(lambda).cdf(x) # cummulative

# uniform dist
stats.uniform(a, b).pdf(x)
stats.uniform(a, b).cdf(x) # cummulative