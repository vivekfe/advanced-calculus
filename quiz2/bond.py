import numpy as np
from math import *

def bond_price(ls_cashflow, ls_time, f_yield):
	f_ret = 0.
	for i in range(len(ls_cashflow)):
		f_ret += ls_cashflow[i]*exp(-ls_time[i]*f_yield)
	return f_ret

def bond_duration(ls_cashflow, ls_time, f_yield):
	f_ret = 0.
	for i in range(len(ls_cashflow)):
		f_ret += ls_cashflow[i]*ls_time[i]*(1.+f_yield/2.)**(-2*ls_time[i]-1)
	return f_ret/bond_price(ls_cashflow, ls_time, f_yield)

def bond_convexity(ls_cashflow, ls_time, f_yield):
	f_ret = 0.
	for i in range(len(ls_cashflow)):
		f_ret += ls_cashflow[i]*ls_time[i]*(ls_time[i]+1.0/2)*(1.+f_yield/2.)**(-2*ls_time[i]-2)
	return f_ret/bond_price(ls_cashflow, ls_time, f_yield)

def r(time):
	return 0.025+time/(300.-time)

def r_2(time):
	return 0.02+time/(200.-time)

'''
ls_cashflow = [0.15,0.15,0.15,0.15,10.15]
ls_time = [1./12,7./12,13./12,19./12,25./12]#[.5,1,1.5,2,2.5]
f_ret = 0.
for i in range(len(ls_cashflow)):
	f_ret += ls_cashflow[i]*(1+0.5*r(ls_time[i]))**(-ls_time[i]/0.5)
print f_ret

t=1./12
f_float = 10.125*(1+r(t)/2)**(-t/0.5)
print f_ret - f_float
'''

'''
ls_cashflow = [1.,1.,1.,1.,1.,1.,101.]
ls_time = [1./12,4./12,7./12,10./12,13./12,16./12,19./12]
f_ret = 0.
for i in [6,5,4,3,2,1,0]:
	print ls_cashflow[i]*exp(-ls_time[i]*r_2(ls_time[i]))
	f_ret += ls_cashflow[i]*exp(-ls_time[i]*r_2(ls_time[i]))
print f_ret
'''


ls_cashflow = [2.,2.,2.,102]
ls_time = [1./12, 7./12, 13./12, 19./12]
f_yield = 0.025
print bond_price(ls_cashflow, ls_time, f_yield), bond_duration(ls_cashflow, ls_time, f_yield), bond_convexity(ls_cashflow, ls_time, f_yield)
