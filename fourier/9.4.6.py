from math import pi
from matplotlib import pyplot as plt
import numpy as np

A=10
P=10

def fr(x,N):
  
  tot=0
  for n in range(1,N):
    an=0
    bn=2*A*((-1)**(n+1)+1)/(pi*n)
    tot+=(an*np.cos(n*pi*x/(P/2))+bn*np.sin(n*pi*x/(P/2)))
  
  return tot

x=np.linspace(-P,P,1001)
for cn,cc in zip([15,20],['b','g']):
  plt.plot(x,fr(x,cn),cc)
x=np.linspace(-P,P,4001)
y0=np.linspace(-A,-A,1001)
y1=np.linspace(A,A,1001)
y=np.concatenate((y1,y0[1:],y1[1:],y0[1:]))
plt.plot(x,y,'r')
plt.show()