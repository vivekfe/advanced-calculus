B = 100000000
C_dollar = 250000000
DV01 = 25000
delta_y = 0.01/100

D_dollar = -(DV01 - 0.5*C_dollar*delta_y**2)/delta_y
print D_dollar