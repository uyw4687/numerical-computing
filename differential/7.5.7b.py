import matplotlib.pyplot as plt

def f(t,inx):
  x,y,z=inx
  return (10*(y-x), x*(28-z)-y, x*y-8*z/3)

t=0
x=[15,15,36]
n=10
# h=20/n
h=1/n

ax=plt.axes(projection="3d")

for i in range(n):

  k1=f(t,x)
  k2=f(t+h/2,(x[j]+h*k1[j]/2 for j in range(3)))
  k3=f(t+h/2,(x[j]+h*k2[j]/2 for j in range(3)))
  k4=f(t+h,(x[j]+h*k3[j] for j in range(3)))

  i=0
  for elem in zip(k1,k2,k3,k4):
    x[i]=x[i]+(elem[0]+2*elem[1]+2*elem[2]+elem[3])/6
    i+=1
  t+=h
  print(t,x)
  ax.scatter3D(x[0],x[1],x[2])

plt.show()