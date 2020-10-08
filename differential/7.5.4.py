import matplotlib.pyplot as plt

a=-10**-2
b=-10**2/4
c=10**-2
d=-10**2

def f(t,x):
  u,v=x
  return (a*(v+b)*u,c*(u+d)*v)

t=0
x=[80,30]
n=10
h=1

ax=plt.axes(projection="3d")

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
  print(t,x)
  ax.scatter3D(x[0],x[1],t)

plt.show()