import numpy as np
from math import *

startPoint = 0.0
endPoint = 2.0
def function(x): return e**(-x*x)
tol = 5*1e-7

def integMid(a, b, f, nbins=10):
    '''Return the integral from a to b of function f using the midpoint rule'''
    h = float(b-a)/nbins
    assert h > 0
    assert type(nbins) == int
    sum = 0.0
    x = a + h/2
    while (x < b):
        sum += h * f(x)
        x += h
    return sum

f_previous, f_current = 0.0, 0.0
for i in range(2, 200):
	i_spacing = 2**i
	f_current = integMid(startPoint, endPoint, function, nbins=i_spacing)
	print i_spacing, f_current
	if abs(f_current - f_previous) < tol: 
		break
	else: 
		f_previous = f_current