import numpy as np
from math import *

def libor(time):
	return 0.025 + time/(300-time)

f_notional = 10.
f_fixedRate = 0.03

ls_cashflowFixed = [f_notional*f_fixedRate for i in range(4)]
ls_cashflowFixed.append(f_notional*(1+f_fixedRate))

ls_cashflowFloat = [f_notional*(1+0.5*libor(i/2))**i-f_notional for i in range(1,5)]
ls_cashflowFloat.append(f_notional*(1+0.5*libor(2.5))**5)

print ls_cashflowFixed
print ls_cashflowFloat
