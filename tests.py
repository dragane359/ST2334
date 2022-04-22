from conf_intervals import *

print(known_mean_variance(3.5, 0.025, 36, .3))
print(unknown_mean_variance_lessthan30(10, 0.025, 6, 7, sqrt(0.08)))
print(unknown_mean_variance_morethan30(62.56, 0.05, 50, 20))
print(diffbtw_known_mean_variance(42, 36, 0.02, 50, 75, 6, 8))
print(diffbtw_unknown_mean_variance_morethan30(78.3, 87.2, 0.025, 50, 50, 5.6, 6.3))
print(diffbtw_unknown_butequal_variance_lessthan30(85, 81, 0.05, 12, 10, 4, 5))
print(diffbtw_unknown_butequal_variance_morethan30(85, 81, 0.05, 12, 10, 4, 5))
print(diffbtw_unknown_paired_lessthan30(-1.6, 10, 0.01, sqrt(40.71)))
print(diffbtw_unknown_paired_morethan30(-1.6, 10, 0.01, sqrt(40.71)))
print(confint_sdsquared_mean_unknown(10, 0.025, sqrt(0.286)))
print(confint_sdsquared_mean_known(10, 0.025, sqrt(0.286)))
print(confint_ratioof2sd_mean_known(0.01, 25, 16, 8, 7))

