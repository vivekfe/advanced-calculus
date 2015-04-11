import mibian

S = 35.
K = 40.
r = 2.
T = 3./12 * 365
v = 30.
Num_shares = 400
Cash = 10000.

'''
#1
put = mibian.BS([S, K, r, T], volatility=v)
print put.putPrice
portfolio = 2000*put.putPrice + 400*S + 10000
print portfolio

#2
portfolioDelta = 2000*put.putDelta + 400
print portfolioDelta
cash = 10000. - 1166*S
print cash
'''

#3
put = mibian.BS([S, K, r, T], volatility=v)
portfolioDelta = 2000*put.putDelta + Num_shares
print "hedge:", -round(portfolioDelta)
Num_shares -= round(portfolioDelta)
Cash += round(portfolioDelta)*S
print "A0:",round(2000*put.putPrice,2), round(Num_shares*S,2), round(Cash,2)
print "current shares:", Num_shares

S = 40
T -= 1./52
put = mibian.BS([S, K, r, T], volatility=v)
Cash *= (1+r/100)**(1./52)
print "B1:",round(2000*put.putPrice,2), round(Num_shares*S,2), round(Cash,2)
print "current shares:", Num_shares
portfolioDelta = 2000*put.putDelta + Num_shares
print "hedge:",-round(portfolioDelta)
Num_shares -= round(portfolioDelta)
Cash += round(portfolioDelta)*S
print "A1:",round(2000*put.putPrice,2), round(Num_shares*S,2), round(Cash,2)
print "current shares:", Num_shares

S = 36
T -= 1./52
put = mibian.BS([S, K, r, T], volatility=v)
Cash *= (1+r/100)**(1./52)
print "B2:",round(2000*put.putPrice,2), round(Num_shares*S,2), round(Cash,2)
print "current shares:", Num_shares
portfolioDelta = 2000*put.putDelta + Num_shares
print "hedge:",-round(portfolioDelta)
Num_shares -= round(portfolioDelta)
Cash += round(portfolioDelta)*S
print "A2:",round(2000*put.putPrice,2), round(Num_shares*S,2), round(Cash,2)
print "current shares:", Num_shares

S = 32
T -= 1./52
put = mibian.BS([S, K, r, T], volatility=v)
Cash *= (1+r/100)**(1./52)
print "B3:",round(2000*put.putPrice,2), round(Num_shares*S,2), round(Cash,2)
print "current shares:", Num_shares
portfolioDelta = 2000*put.putDelta + Num_shares
print "hedge:", -round(portfolioDelta)
Num_shares -= round(portfolioDelta)
Cash += round(portfolioDelta)*S
print "A3:",round(2000*put.putPrice,2), round(Num_shares*S,2), round(Cash,2)
print "current shares:", Num_shares

S = 37
T -= 1./52
put = mibian.BS([S, K, r, T], volatility=v)
Cash *= (1+r/100)**(1./52)
print "B4:",round(2000*put.putPrice,2), round(Num_shares*S,2), round(Cash,2)
print "current shares:", Num_shares
portfolioDelta = 2000*put.putDelta + Num_shares
print "hedge:", -round(portfolioDelta)
Num_shares -= round(portfolioDelta)
Cash += round(portfolioDelta)*S
print "A4:",round(2000*put.putPrice,2), round(Num_shares*S,2), round(Cash,2)
print "current shares:", Num_shares