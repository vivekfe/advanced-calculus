from math import *

def simpson(f, d_a, d_b, i_n):
	i_n *= 2
	d_h = (d_b - d_a) / i_n
	d_k, d_x = 0.0, d_a + d_h
	for i in range(1, i_n/2 + 1):
		d_k += 4*f(d_x)
		d_x += 2*d_h
	d_x = d_a + 2*d_h
	for i in range(1, i_n/2):
		d_k += 2*f(d_x)
		d_x += 2*d_h
	return (d_h/3)*(f(d_a)+f(d_b)+d_k)

def function(x): return exp(-x*x/2)


for j in [0.1, 0.5, 1.0]:
	print "Compute N(", j, "):"
	d_previous, d_current = 0.0, 0.0
	for i in range(2,200):
	    i_n = 2**i
	    d_current = 0.5 + simpson(function, 0.0, j, i_n) / sqrt(2*pi)
	    print i_n, d_current
	    if abs(d_current-d_previous) < 10**(-12): break
	    else: d_previous = d_current