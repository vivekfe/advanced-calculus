from math import *

floating = (2.5 + 100)*exp(-0.04 * 4./12)
fixed = 2.5*exp(-0.04 * 4./12) + 2.5*exp(-0.04 * 10./12) + 102.5*exp(-0.04 * 16./12)

print floating, fixed
print floating - fixed 