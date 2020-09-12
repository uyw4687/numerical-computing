import numpy as np
from math import pi,cos
# import matplotlib.pyplot as plt

# x=np.linspace(0,pi/2,100)
# y=x*np.cos(x)
# print(x)
# print(y)

# plt.plot(x,y)
# plt.show()

ndiv=5
a=0
b=pi/2
err=(b-a)/ndiv
while True:
  x=np.linspace(a,b,ndiv)
  y=x*np.cos(x)
  ind=ndiv-1
  for i in range(ndiv-1):
    if y[i]>=y[i+1]:
      ind=i
      break
  a=x[max(0,ind-1)]
  b=x[min(ndiv-1,ind+1)]
  err=(b-a)/ndiv
  if err<10**-7:
    break
c=(a+b)/2
fc=c*cos(c)

def p(a):
  return "%0.6f"%a

print(p(c))
print(p(fc))