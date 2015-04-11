import numpy as np
from math import *
from scipy.optimize import newton
from decimal import *

getcontext().prec = 15

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

ls_cashflow = []
ls_time = []
for i in range(8):
	ls_cashflow.append(100*0.08/4)
	ls_time.append((i+1)*3./12)
ls_cashflow[-1] += 100

f_yield = 0.09

B = bond_price(ls_cashflow, ls_time, f_yield)
D = bond_duration(ls_cashflow, ls_time, f_yield)
C = bond_convexity(ls_cashflow, ls_time, f_yield)
print B, D, C

for delta_y in [0.001, 0.005, 0.01, 0.02, 0.04]:
	B1 = round(B - B*D*delta_y,12)
	B2 = round(B + B*(-D*delta_y + 0.5*C*(delta_y)**2),12)
	B3 = round(bond_price(ls_cashflow, ls_time, f_yield+delta_y),12)
	#print delta_y, "B_new_D:", B1
	#print delta_y, "B_new_D_C:", B2
	#print delta_y, "B(y+delta_y)", B3
	print delta_y, round(abs(B1-B3)/B3,12), round(abs(B2-B3)/B3,12)