from math import *
from scipy.stats import norm

# Black Sholes Function
def BlackSholes(CallPutFlag,S,X,T,r,v):
    d1 = (log(S/X)+(r+v*v/2.)*T)/(v*sqrt(T))
    #print 1000*norm.cdf(-d1)
    d2 = d1-v*sqrt(T)
    if CallPutFlag=='c':
        return S*norm.cdf(d1)-X*exp(-r*T)*norm.cdf(d2)
    else:
        return X*exp(-r*T)*norm.cdf(-d2)-S*norm.cdf(-d1)

print BlackSholes('p',100.,100.,0.5,0.05,0.3), BlackSholes('p',102.,100.,125./252,0.05,0.3)
print 1000*BlackSholes('p',102.,100.,125./252,0.05,0.3)+411*102.-411*100.*exp(0.05*1/365)
print 1000*(BlackSholes('p',102.,100.,125./252,0.05,0.3) - BlackSholes('p',100.,100.,0.5,0.05,0.3))
print (1000*BlackSholes('p',102.,100.,125./252,0.05,0.3)+411*102-411*100*exp(0.05/252)) - 1000*BlackSholes('p',100.,100.,0.5,0.05,0.3)