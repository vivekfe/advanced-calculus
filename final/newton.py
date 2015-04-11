import numpy as np
from math import *
#from scipy.optimize import newton
from scipy.misc import derivative


def newton(func, funcd, x, TOL=1e-6):   # f(x)=func(x), f'(x)=funcd(x)
    count = 0
    f_previous, f_current = func(x), 0.0
    while 1:
    	fd = funcd(x)
    	dx = f_previous / float(fd)
    	x -= dx
    	f_current = func(x)
    	count += 1
    	print "newton(%d): x=%s, f(x)=%s" % (count, x, f_current)
        if abs(f_current-f_previous) < TOL: 
            return x
        f_previous = f_current
        


def func(x):
    ls_cashflow = []
    ls_time = []
    for i in range(10*12):
        ls_cashflow.append(2000)
        ls_time.append((i+1)*1./12)
    ls_cashflow[-1] += 200000
    f_ret = 0.
    for i in range(len(ls_cashflow)):
        f_ret += ls_cashflow[i]*exp(-ls_time[i]*x)
        #f_ret += ls_cashflow[i]*(1+0.5*x)**(-2*ls_time[i])
    return f_ret-378317.159489

def fprime(x):
    def f(x):
        ls_cashflow = []
        ls_time = []
        for i in range(10*12):
            ls_cashflow.append(2000)
            ls_time.append((i+1)*1./12)
        ls_cashflow[-1] += 200000
        f_ret = 0.
        for i in range(len(ls_cashflow)):
            f_ret += ls_cashflow[i]*exp(-ls_time[i]*x)
            #f_ret += ls_cashflow[i]*(1+0.5*x)**(-2*ls_time[i])
        return f_ret-378317.159489
    return derivative(f, x)

f_yield = newton(func=func, funcd = fprime, x=0.05, TOL=1e-6)
print f_yield