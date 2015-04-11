import numpy as np
from math import *
from scipy.integrate import simps

startPoint = 0.01
endPoint = 0.1
def function(r):
	return ( (sin(r/0.016))**2+0.5 ) * e**(-(r-0.05)**2)
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

a = simpson(startPoint, endPoint, function, tol)