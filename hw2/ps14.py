from math import *
from scipy.stats import norm

print norm.cdf(1)
print norm.cdf(1) + 1./sqrt(2*pi)*exp(-0.5)
print 1./sqrt(2*pi)*exp(-0.5) /2