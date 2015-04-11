from scipy.optimize import newton
from scipy.misc import derivative
#from scipy.optimize import secant
from mibian import *

def func(implied_volatility):
	spotPrice = 30.
	strike = 27.
	riskFreeRate = 0.04 * 100
	dividendsYield = 0.01 * spotPrice
	maturity = 7./12 * 365
	option = Me([spotPrice, strike, riskFreeRate, dividendsYield, maturity], volatility=implied_volatility)
	return option.callPrice - 4.5

print newton(func=func, x0=50)
#print secant(func=func, x0=0.5, x1=0.501)
