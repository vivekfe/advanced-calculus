from mibian import *
import numpy as np
from numpy.linalg import solve


#1
call = Me([50., 55., 4., 0.02*50., 6./12*365], volatility=20.)
put = Me([50., 45., 4., 0.02*50., 6./12*365], volatility=20.)

d_portfolioDelta = 1000*call.callDelta + 600*put.putDelta
shares_1 = -round(d_portfolioDelta)
cash_1 = -shares_1*50.
#print call.callPrice, put.putPrice, call.callDelta, put.putDelta


#2
ATMcall = Me([50., 50., 4., 0.02*50., 9./12*365], volatility=20.)
#print call.callDelta, put.putDelta, ATMcall.callDelta
#print call.gamma, put.gamma, ATMcall.gamma

a = np.array([[1,ATMcall.callDelta], [0,ATMcall.gamma]])
b = np.array([-1000*call.callDelta-600*put.putDelta, -1000*call.gamma-600*put.gamma])
x = solve(a, b)
#print x
shares_2 = round(x[0])
Num_ATMcall = round(x[1])
cash_2 = -shares_2*50. - Num_ATMcall*ATMcall.callPrice

#3
call = Me([50., 55., 4., 0.02*50., 6./12*365], volatility=20.)
put = Me([50., 45., 4., 0.02*50., 6./12*365], volatility=20.)
ATMcall = Me([50., 50., 4., 0.02*50., 9./12*365], volatility=20.)
v_portfolio_1b = 1000*call.callPrice + 600*put.putPrice
v_portfolio_2b = 1000*call.callPrice + 600*put.putPrice + shares_1*50. + cash_1
v_portfolio_3b = 1000*call.callPrice + 600*put.putPrice + shares_2*50. + Num_ATMcall*ATMcall.callPrice + cash_2
call = Me([54., 55., 4., 0.02*54., (6./12-1./252)*365], volatility=30.)
put = Me([54., 45., 4., 0.02*54., (6./12-1./252)*365], volatility=30.)
ATMcall = Me([54., 50., 4., 0.02*54., (9./12-1./252)*365], volatility=30.)
v_portfolio_1a = 1000*call.callPrice + 600*put.putPrice
v_portfolio_2a = 1000*call.callPrice + 600*put.putPrice + shares_1*54.*(1+0.02)**(1./252) + cash_1*(1+0.04)**(1./252)
v_portfolio_3a = 1000*call.callPrice + 600*put.putPrice + shares_2*54.*(1+0.02)**(1./252) + Num_ATMcall*ATMcall.callPrice + cash_2*(1+0.04)**(1./252)
print "v_portfolio_1b:", v_portfolio_1b
print "v_portfolio_1a:", v_portfolio_1a
print "v_portfolio_1a - v_portfolio_1b:", v_portfolio_1a - v_portfolio_1b
print "v_portfolio_2b:", v_portfolio_2b
print "v_portfolio_2a:", v_portfolio_2a
print "v_portfolio_2a - v_portfolio_2b:", v_portfolio_2a - v_portfolio_2b
print "v_portfolio_3b:", v_portfolio_3b
print "v_portfolio_3a:", v_portfolio_3a
print "v_portfolio_3a - v_portfolio_3b:", v_portfolio_3a - v_portfolio_3b
