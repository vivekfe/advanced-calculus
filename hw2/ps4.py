from mibian import *
from scipy.optimize import newton

def function(strike):
	spotPrice = 30.
	volatility = 30.
	dividendsYield = 0.01*spotPrice
	riskFreeRate = 2.5
	maturity = 3./12 * 365
	option = Me([spotPrice, strike, riskFreeRate, dividendsYield, maturity], volatility=volatility)
	return option.callDelta - 0.5

print "strike:", newton(function, 30.)