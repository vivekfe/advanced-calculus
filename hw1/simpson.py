from math import *
from scipy.integrate import simps

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

def r(t):
	return 0.05/(1+exp(-(1+t)**2))

ls_disc = []
for j in [3./12, 9./12, 15./12, 21./12]:
	d_previous, d_current = 0.0, 0.0
	for i in range(200):
	    i_n = 2**i
	    d_current = exp(-simpson(r, 0.0, j, i_n))
	    print i_n, d_current
	    if abs(d_current-d_previous) < 1e-12: break
	    else: d_previous = d_current
	ls_disc.append(d_current)

f_ret = 0.
ls_cash_flow = [2.5, 2.5, 2.5, 102.5]
for i in range(len(ls_disc)):
	f_ret += ls_cash_flow[i] * ls_disc[i]
print f_ret