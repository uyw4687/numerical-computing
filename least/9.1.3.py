from matplotlib import pyplot as plt
import numpy as np

m=10
x=np.linspace(-5,5,m+1)
y=np.linspace(5,0,m+1)
y=y+np.random.randint(-3,3,m+1)
print(x)
print(y)
plt.plot(x,y,'o')

p=x.sum()
q=y.sum()
r=(x*y).sum()
s=(x*x).sum()
d=(m+1)*s-p*p
a=((m+1)*r-p*q)/d
b=(s*q-p*r)/d
print(a,b)

x=np.linspace(-5,5,m+1)
y=a*x+b
plt.plot(x,y)

plt.show()