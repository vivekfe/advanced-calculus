import numpy as np

notional = 10000000.
ls_fixed = [0.02*notional, 0.02*notional, 0.02*notional, 1.02*notional]
ls_time = [0.5, 1.0, 1.5, 2.0]


def r(observed_time, t):
	if observed_time < 0.5:
		return 0.01 + t/100.
	elif observed_time < 1.0:
		return 0.02 + (t-observed_time)/200.
	elif observed_time < 1.5:
		return 0.025 + (t-observed_time)/100.
	else:
		return 0.02 + (t-observed_time)/400.

#1
ls_float = []
for i in range(len(ls_time)):
	ls_float.append(notional*0.5*(r(ls_time[i]-0.5, ls_time[i])))
ls_float[-1] += notional
print ls_fixed, ls_float
print np.array(ls_fixed) - np.array(ls_float)

#2
def r_2(t):
	return 0.025 + t/200.

v_fixed = 0
for i in range(len(ls_fixed)):
	print r_2(ls_time[i]-4./12)
	v_fixed += notional*(1+r_2(ls_time[i]-4./12)/2.)**(-(ls_time[i]-4./12)/(0.5))
print v_fixed

v_float = (ls_float[0]+notional)*(1+r_2(2./12)/2.)**(-(2./12)/(0.5))
print v_float

print v_fixed - v_float