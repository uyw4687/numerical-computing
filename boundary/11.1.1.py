from math import e,log,pi

t=0
x1=log(8*pi**2)
x2=-25/2
n=100
h=1/n

print(log(8*pi**2))

for i in range(n):

  x1p=x2
  x2p=e**x1

  # print(t,x1,x1+h*x1p,x2,x2+h*x2p)

  x1=x1+h*x1p
  x2=x2+h*x2p

  t+=h

print(t,x1,x2)

# a=0.9372375321588863
# b=6.3678668146937785
# c=log(8*pi**2)

# d=(c-a)/(b-a)
# print((-25/2)*(1-d)+(-23/2)*(d))