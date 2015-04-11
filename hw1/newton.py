import numpy as np
from math import *
from scipy.optimize import newton

def func(x):
    ls_cashflow = [1.75, 1.75, 1.75, 1.75, 101.75]
    ls_time = [1./12,7./12,13./12,19./12,25./12]
    f_ret = 0.
    for i in range(len(ls_cashflow)):
        #f_ret += ls_cashflow[i]*exp(-ls_time[i]*x)
        f_ret += ls_cashflow[i]*(1+0.5*x)**(-2*ls_time[i])
    return f_ret-101.431199988

print newton(func=func, x0=0.5)