from mibian import *
from math import *


dS = 10**(-1)
V_SplusdS = 2.9215320
V_S = 2.9650717
V_SminusdS = 3.0117945

delta = (V_SplusdS - V_SminusdS)/(2*dS)
gamma = (V_SplusdS - 2*V_S + V_SminusdS)/(dS**2)
print delta, gamma
'''

dT = 1.
V_TmimusdT = 2.9574734
V_T = 2.9650717

theta = (V_TmimusdT - V_T) / dT
print theta
'''