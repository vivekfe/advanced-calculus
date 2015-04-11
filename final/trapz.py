import numpy as np
from math import *
from numpy import trapz

startPoint = 0.0
endPoint = 2.0
def function(x): return e**(-x*x)
tol = 5*1e-7

f_previous, f_current = 0.0, 0.0
for i in range(2, 200):
	i_spacing = 2**i
	na_x = np.linspace(startPoint, endPoint, i_spacing+1)
	ls_y = [function(x) for x in na_x]
	f_current = trapz(ls_y, na_x)
	print i_spacing, f_current
	if abs(f_current - f_previous) < tol: 
		break
	else: 
		f_previous = f_current