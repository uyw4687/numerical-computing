from matplotlib import pyplot as plt
from random import random
from math import sqrt
import numpy as np

n=0
while n<=10**3:
  x=random()*6-3 #[-3,3)
  y=random()*6-3 #[-3,3)

  r=sqrt(x**2+y**2)
  c=x/r
  if r<=2-c:
    plt.plot(x,y,'.',ms=1)
    n+=1

th=np.linspace(0,2*np.pi,1001)
r=2-np.cos(th)
x=r*np.cos(th)
y=r*np.sin(th)
plt.plot(x,y)

plt.show()