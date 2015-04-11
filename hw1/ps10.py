from scipy.optimize import newton
from math import *

def func(R):
	return 2.5*exp(-4.5/100*(.5)) + 2.5*exp(-4.5/100*(1.0)) + 102.5*exp(-1.5*R) - 100.

print newton(func, 0.05)