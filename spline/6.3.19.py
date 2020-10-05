from math import factorial as fac
import matplotlib.pyplot as plt
def pol(i,x):
  return (x**i)*((1-x)**(n-i))*fac(n)/fac(i)/fac(n-i)

v=[(3,3),(2,3),(0,3),(0,2),(3,2),(3.5,1.5),(3.2,1.2),(3,1),(2,1),(1,0)]
n=len(v)-1

t=0
th=10**-3
while t<=1:
  x=y=0
  for i in range(len(v)):
    x+=pol(i,t)*v[i][0]
    y+=pol(i,t)*v[i][1]
  t+=th
  plt.plot(x,y,".b")
plt.show()