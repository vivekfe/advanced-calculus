from scipy.optimize import bisect
from scipy.optimize import newton
#from scipy.optimize import secant
from mibian import *
from math import *

def func(implied_volatility):
	spotPrice = 40.
	strike = 40.
	riskFreeRate = 0.025 * 100
	dividendsYield = 0.01 * spotPrice
	maturity = 5./12 * 365
	option = Me([spotPrice, strike, riskFreeRate, dividendsYield, maturity], volatility=implied_volatility)
	return option.callPrice - 2.75

print bisect(func, 0.01, 100)
newton = newton(func, 50) / 100
print newton
#print secant(func, 50, 49)

spotPrice = 40.
strike = 40.
riskFreeRate = 0.025
dividendsYield = 0.01
maturity = 5./12
callPrice = 2.75
appoxi = (2*pi)**(0.5) / (spotPrice*maturity**0.5) * (callPrice - (riskFreeRate-dividendsYield)*maturity/2*spotPrice) / (1-(riskFreeRate+dividendsYield)*maturity/2)

print abs(appoxi - newton)/(newton)