from math import *
import numpy as np
from scipy.integrate import simps

T = 3./12
S = 50
q = 0.02
sigma = 0.3
r = 0.04
K = 50

d2 = (log(S/K) - (r-q-sigma**2/2)*T) / (sigma*sqrt(T))