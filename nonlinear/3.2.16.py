# import numpy as np
# import matplotlib.pyplot as plt

# x=np.linspace(-2,2,50)
# y=x**5-9*x**4-x**3+17*x**2-8*x-8
# print(x)
# print(y)

# plt.plot(x,y)
# plt.show()

x=-0.5
# while True:
for i in range(10):
  y=x**5-9*x**4-x**3+17*x**2-8*x-8
  ydx=5*x**4-36*x**3-3*x**2+34*x-8
  err=y/ydx
  if abs(err)<10**(-15):
    break
  x=x-y/ydx
  print(y)
  print(x)