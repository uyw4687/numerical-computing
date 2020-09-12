import numpy as np
# import matplotlib.pyplot as plt
# from math import pi

# x=np.linspace(50,200,10)
# y=x*np.cosh(50/x)
# print(x)
# print(y)

# plt.plot(x,y)
# plt.show()

a=50
b=200
err=b-a
fa=a*np.cosh(50/a)-a-10
fb=b*np.cosh(50/b)-b-10
signfa=np.sign(fa)

def p(a):
  return "%0.6f"%a

while True:
  err/=2
  c=a+err
  fc=c*np.cosh(50/c)-c-10
  print('a',p(a),'c',p(c),'b',p(b),'err',p(err))
  if err<10**-4:
    break
  signfc=np.sign(fc)
  if signfc==signfa:
    a=c
    fa=fc
    signfa=signfc
  else:
    b=c
    fb=fc