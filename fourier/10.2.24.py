from random import random
from math import log,e,sin

def f(x):
  num=e**(sin(x)+x**2)
  den=log(x)
  return num/den

N=10**6

a=3.2
b=5.9
c=e**(1+b**2)/log(a)

lenx=b-a
ofsx=a
leny=c-0
ofsy=0

cnt=0
for n in range(N):
  x=random()*lenx+ofsx
  y=random()*leny+ofsy
  if y<=f(x):
    cnt+=1

vol=lenx*leny
print(vol*cnt/N)