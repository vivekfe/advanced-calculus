import numpy as np
from math import *

def bond_price(ls_cashflow, ls_time, f_yield):
	f_ret = 0.
	for i in range(len(ls_cashflow)):
		f_ret += ls_cashflow[i]*(1.+f_yield/2.)**(-2*ls_time[i])
		#f_ret += ls_cashflow[i]*exp(-ls_time[i]*f_yield)
	return f_ret

def bond_duration(ls_cashflow, ls_time, f_yield):
	f_ret = 0.
	for i in range(len(ls_cashflow)):
		f_ret += ls_cashflow[i]*ls_time[i]*(1.+f_yield/2.)**(-2*ls_time[i]-1)
		#f_ret += ls_cashflow[i]*ls_time[i]*exp(-f_yield*ls_time[i])
	return f_ret/bond_price(ls_cashflow, ls_time, f_yield)

def bond_convexity(ls_cashflow, ls_time, f_yield):
	f_ret = 0.
	for i in range(len(ls_cashflow)):
		f_ret += ls_cashflow[i]*ls_time[i]*(ls_time[i]+1.0/2)*(1.+f_yield/2.)**(-2*ls_time[i]-2)
		#f_ret += ls_cashflow[i]*(ls_time[i]**2)*exp(-f_yield*ls_time[i])
	return f_ret/bond_price(ls_cashflow, ls_time, f_yield)

def r(time):
	return 0.015+time/(100.+(1.+time**2)**(0.5))

'''
ls_cashflow = [1.75, 1.75, 1.75, 1.75, 101.75]
ls_time = [1./12,7./12,13./12,19./12,25./12]
f_ret = 0.
for i in range(len(ls_cashflow)):
	#f_ret += ls_cashflow[i]*exp(-ls_time[i]*r(ls_time[i]))
	f_ret += ls_cashflow[i]*(1.+r(ls_time[i])/2.)**(-2*ls_time[i])
print f_ret


'''
ls_cashflow = [1.75, 1.75, 1.75, 1.75, 101.75]
ls_time = [1./12,7./12,13./12,19./12,25./12]
f_yield = 0.0351255618514
print bond_price(ls_cashflow, ls_time, f_yield), bond_duration(ls_cashflow, ls_time, f_yield), bond_convexity(ls_cashflow, ls_time, f_yield)
