from random import random
from math import sin

def f(x):
  # return x**2
  # return 2*x**2-x+1
  return x**2+sin(2*x)

N=10**4

# a=1
# b=2
# c=4

# a=0
# b=1
# c=2

a=0
b=1
c=2

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