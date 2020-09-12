from math import log
# import numpy as np
# import matplotlib.pyplot as plt

# x=np.linspace(0.01,1,50)
# y=2*x*(1-x*x+x)*np.log(x)-x*x+1
# print(x)
# print(y)

# plt.plot(x,y)
# plt.show()

x=0.4
while True:
  y=2*x*(1-x*x+x)*log(x)-x*x+1
  ydx=2*(1-3*x*x+2*x)*log(x)+2*(1-x*x)
  err=y/ydx
  if abs(err)<10**(-15):
    break
  x=x-y/ydx
  print(x)