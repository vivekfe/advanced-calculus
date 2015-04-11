from mibian import *

spotPrice = 50.
dividendsYield = 0.02 * spotPrice
volatility = 0.3 * 100
riskFreeRate = 0.04 * 100
ls_strike = [40.,45.,50.,55.,60.]
maturity = 3./12 * 365

for f_strike in ls_strike:
	option = Me([spotPrice, f_strike, riskFreeRate, dividendsYield, maturity], volatility=volatility)
	straddleDelta = option.putDelta + option.callDelta
	straddleGamma = option.gamma + option.gamma
	print f_strike, "straddleDelta:", round(straddleDelta,6)
	print f_strike, "straddleGamma:", round(straddleGamma,6)