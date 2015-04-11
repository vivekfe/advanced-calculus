B = 100000000
C_dollar = 250000000
DV01 = 25000
D_dollar = DV01 * 10000
delta_y = -30./10000

delta_B = -D_dollar*delta_y + 0.5*C_dollar*delta_y**2
print delta_B

C_dollar = -500000000
delta_y = 30./10000
print 0.5*C_dollar*(delta_y**2)