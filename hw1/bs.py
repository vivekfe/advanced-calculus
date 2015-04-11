from math import *
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Black Sholes Function
def BlackSholes(CallPutFlag,S,X,T,r,v):
    d1 = (log(S/X)+(r+v*v/2.)*T)/(v*sqrt(T))
    d2 = d1-v*sqrt(T)
    if CallPutFlag=='c':
        return S*norm.cdf(d1)-X*exp(-r*T)*norm.cdf(d2)
    else:
        return X*exp(-r*T)*norm.cdf(-d2)-S*norm.cdf(-d1)

def Premium(S):
	return BlackSholes(CallPutFlag='c',S=S,X=100.,T=0.5,r=0.05,v=0.3) - max(S-100.,0.)

def Premium_put(S):
	return BlackSholes(CallPutFlag='p',S=S,X=100.,T=0.5,r=0.05,v=0.3) - max(100.-S,0.)

x = np.linspace(50, 200)
y = [Premium_put(i) for i in x]

fig, ax = plt.subplots()
plt.plot(x, y, 'r', linewidth=2)

plt.savefig('5-4.pdf')