from random import random

N=10**6

a=-1
b=1
c=-2
d=2

lenx=b-a
ofsx=a
leny=d-c
ofsy=c

cnt=0
for n in range(N):
  a=random()*lenx+ofsx
  b=random()*leny+ofsy
  if b**2-4*a>=0:
    cnt+=1

print(cnt/N)