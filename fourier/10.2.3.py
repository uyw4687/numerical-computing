from random import random
from math import pi

N=2500
cnt=0
for n in range(N):
  x=random()*2 #[0,2)
  y=random()*2 #[0,2)
  if y**2<=4-x**2:
    cnt+=1
  
vol=4
print("monte",cnt/N*vol)
print("anal",pi)