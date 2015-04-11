from scipy.optimize import newton
from mibian import *
from scipy.misc import derivative

spotPrice = 50.
riskFreeRate = 0.02 * 100
dividendsYield = 0.02 * spotPrice
maturity = 3./12 * 365
volatility = 0.3 * 100

def func(strike):
	option = Me([spotPrice, strike, riskFreeRate, dividendsYield, maturity], volatility=volatility)
	return option.callDelta - 0.5

print newton(func=func, x0=0.5)