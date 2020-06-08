#nCr mod 高速
def cmb(n,r,mod):
    x=1
    y=1
    for i in range(1,r+1):
        x=(x*(n-i+1))%mod
        y=(y*i)%mod
    return (x*pow(y,mod-2,mod))%mod

#nCr普通
from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under
    
#gcd複数（１，２，３，４）みたいな
def gcd(*numbers):
    return reduce(math.gcd, numbers)

