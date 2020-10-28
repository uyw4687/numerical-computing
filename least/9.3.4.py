import numpy as np
from matplotlib import pyplot as plt

def f(x,y):
  return 1
def g(x,y):
  return x
def h(x,y):
  return -x*y

fs=[f,g,h]

x=[1000,1650,1800,1900,1950,1960,1970,1980,1990,2000,2010]
y=[0.340,0.545,0.907,1.61,2.56,3.15,3.65,4.20,5.30,6.12,6.98]
x=np.array(x)
y=np.array(y)
plt.plot(x,y,'o')

m=len(x)
A=np.zeros((m,3))
b=y

for j in range(3):
  cf = fs[j]
  for i in range(m):
    A[i][j] = cf(x[i],y[i])

cs,_,_,_ = np.linalg.lstsq(A,b,rcond=None)

print(cs)
a,b,c = cs
x=np.linspace(1000,2035,201)
y=(a+b*x)/(1+c*x)
plt.plot(x,y)
plt.show()