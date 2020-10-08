import matplotlib.pyplot as plt
from math import e
a,b=0,10
n=10
t,x=0,[1]*(n+1)
h=1/100
while t<=b:
  for i in range(1,n+1):
    x[i]=x[i-1]
  tmp=x[n]
  for i in range(n-1,-1,-1):
    tmp=h*tmp/(i+1)+x[i]
  x[0]=tmp
  t+=h
  print(t,x[0])
  plt.plot(t,x[0],".b")
  plt.plot(t,e**t,".r")
plt.show()