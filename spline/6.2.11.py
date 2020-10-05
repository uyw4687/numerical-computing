import matplotlib.pyplot as plt
import numpy as np

def f(x):
  if x<-1 or x>1:
    print("wrong input")
    return None
  if x<0:
    return -x**3-3*x**2-x+2
  else:
    return x**3-3*x**2-x+2

x=np.linspace(-1,1,50)
y=[f(v) for v in x]

plt.plot(x,y)
plt.show()