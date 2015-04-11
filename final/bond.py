import numpy as np
from math import *
from scipy.optimize import newton

def bond_price(ls_cashflow, ls_time, f_yield):
	f_ret = 0.
	for i in range(len(ls_cashflow)):
		f_ret += ls_cashflow[i]*exp(-ls_time[i]*f_yield)
		#f_ret += ls_cashflow[i]*(1.+f_yield/2.)**(-2*ls_time[i])
	return f_ret

def bond_duration(ls_cashflow, ls_time, f_yield):
	f_ret = 0.
	for i in range(len(ls_cashflow)):
		f_ret += ls_cashflow[i]*ls_time[i]*exp(-ls_time[i]*f_yield)
		#f_ret += ls_cashflow[i]*ls_time[i]*(1.+f_yield/2.)**(-2*ls_time[i]-1)
	return f_ret/bond_price(ls_cashflow, ls_time, f_yield)

def bond_convexity(ls_cashflow, ls_time, f_yield):
	f_ret = 0.
	for i in range(len(ls_cashflow)):
		f_ret += ls_cashflow[i]*ls_time[i]*ls_time[i]*exp(-ls_time[i]*f_yield)
		#f_ret += ls_cashflow[i]*ls_time[i]*(ls_time[i]+1.0/2)*(1.+f_yield/2.)**(-2*ls_time[i]-2)
	return f_ret/bond_price(ls_cashflow, ls_time, f_yield)

def r_zero_rate(time):
	return log(2.+time**3)/300.

def r_instantaneous_rate(time):
	return 0.025+time/(300.-time)

def bond_price_given_zero_rate_curve(ls_cashflow, ls_time, r_zero_rate):
	f_ret = 0.
	for i in range(len(ls_cashflow)):
		f_ret += ls_cashflow[i]*exp(-ls_time[i]*r_zero_rate(ls_time[i]))
		#f_ret += ls_cashflow[i]*(1+0.5*r(ls_time[i]))**(-ls_time[i]/0.5)
	return f_ret

def bond_price_given_instantaneous_rate_curve(ls_cashflow, ls_time, r_instantaneous_rate):
	for i in range(len(ls_cashflow)):
		r_zero_rate = simpson(0, ls_time[i], r_instantaneous_rate, tol=1e-12)/ls_time[i]
		f_ret += ls_cashflow[i]*exp(-ls_time[i]*r_zero_rate)
		#f_ret += ls_cashflow[i]*(1+0.5*r(ls_time[i]))**(-ls_time[i]/0.5)
	return f_ret

ls_cashflow = []
ls_time = []
for i in range(8):
	ls_cashflow.append(100*0.08)
	ls_time.append((i+1)*3./12)
ls_cashflow[-1] += 100
print ls_time, ls_cashflow

f_yield = 0.09
print bond_price(ls_cashflow, ls_time, f_yield), bond_duration(ls_cashflow, ls_time, f_yield), bond_convexity(ls_cashflow, ls_time, f_yield)
