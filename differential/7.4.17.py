import matplotlib.pyplot as plt

def f(t,x):
  return (x[1],-x[1]-x[0]**2-2*t)

t=0
x=[0,0.1]
n=10
h=3/n

for i in range(n):

  k1=f(t,x)
  k2=f(t+h/2,(x[0]+h*k1[0]/2,x[1]+h*k1[1]/2))
  k3=f(t+h/2,(x[0]+h*k2[0]/2,x[1]+h*k2[1]/2))
  k4=f(t+h,(x[0]+h*k3[0],x[1]+h*k3[1]))

  i=0
  for elem in zip(k1,k2,k3,k4):
    x[i]=x[i]+(elem[0]+2*elem[1]+2*elem[2]+elem[3])/6
    i+=1
  t+=h
  print(x[0],t,x[1])
  plt.plot(x[0],t,".b")

plt.show()