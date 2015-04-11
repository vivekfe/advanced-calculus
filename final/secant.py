"""
Ubiquitous Newton-Raphson algorithm for solving
    f(x) = 0
where a root is repeatedly estimated by
    x = x - f(x)/f'(x)
until |dx|/(1+|x|) < TOL is achieved.  This termination condition is a
compromise between 
    |dx| < TOL,  if x is small
    |dx|/|x| < TOL,  if x is large
"""
def newton(func, funcd, x, TOL=1e-6):   # f(x)=func(x), f'(x)=funcd(x)
    f, fd = func(x), funcd(x)
    count = 0
    while 1:
    dx = f / float(fd)
    if abs(dx) < TOL * (1 + abs(x)): return x - dx
    x = x - dx
    f, fd = func(x), funcd(x)
    count = count + 1
    print "newton(%d): x=%s, f(x)=%s" % (count, x, f)

def secant(func, oldx, x, TOL=1e-6):    # f(x)=func(x)
    oldf, f = func(oldx), func(x)
    if (abs(f) > abs(oldf)):        # swap so that f(x) is closer to 0
    oldx, x = x, oldx
    oldf, f = f, oldf
    count = 0
    while 1:
    dx = f * (x - oldx) / float(f - oldf)
    if abs(dx) < TOL * (1 + abs(x)): return x - dx
    oldx, x = x, x - dx
    oldf, f = f, func(x)
    count = count + 1
    print "secant(%d): x=%s, f(x)=%s" % (count, x, f)