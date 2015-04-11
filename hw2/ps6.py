from math import *
import numpy as np
from scipy.integrate import simps

T = 0.25
K = 45.
S = 50.
sigma = 25./100
q = 1./100
r = 3./100

c1 = exp(-r*T) / sqrt(2*pi)
c2 = log(S/K) + (r-q-sigma**2/2)*T
c3 = sigma*sqrt(T)
d2 = (log(S/K) - (r-q-sigma**2/2)*T) / (sigma*sqrt(T))

startPoint = 1
endPoint = exp(d2)
def function(y):
	print c2-c3*log(y)
	ret = c1 * exp(-(log(y))**2/2) * sqrt(c2-c3*log(y)) / y
	return ret
tol = 1e-12

def simpson(startPoint, endPoint, function, tol):
	f_previous, f_current = 0.0, 0.0
	for i in range(2+1, 200):
		i_spacing = 2**i
		na_x = np.linspace(startPoint, endPoint, i_spacing+1)
		ls_y = [function(x) for x in na_x]
		f_current = simps(ls_y, na_x)
		print i_spacing/2, f_current
		if abs(f_current - f_previous) < tol: 
			break
		else: 
			f_previous = f_current
	return f_current

V0 = simpson(startPoint, endPoint, function, tol)
print V0