from math import *
from scipy.optimize import newton

def r_middle(t, t_start, t_end, r_start, r_end):
	return ((t_end-t)*r_start + (t-t_start)*r_end)/(t_end-t_start)

r_025 = 4*log(100/98.7)
r_05 = 2*log(100/97.5)
def r_05_2(t, r_05, r_2):
	return r_middle(t, 0.5, 2, r_05, r_2)



coupon_rate = 4.875
frequency = 0.5
def function(x, coupon_rate, frequency):
	left = 2.4375*exp(-0.5*r_05) + 2.4375*exp(-1.0*r_05_2(1.0, r_05, x)) + 2.4375*exp(-1.5*r_05_2(1.5, r_05, x)) + (100 + 2.4375)*exp(-2.0*x)
	right = 100 + 5./32
	return left - right
print newton(function, 0.05)

