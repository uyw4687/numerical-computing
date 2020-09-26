import matplotlib.pyplot as plt
import numpy as np

def f1(x):
  return 1/(1+x**2)
def f2(x):
  return (1-x**2)**(1/2)-x

def adapt_simpson(f,a,b,l,max_l,thr,plt):
  itv=b-a
  c=(a+b)/2
  one=itv*(f(a)+4*f(c)+f(b))/6
  d=(a+c)/2
  e=(c+b)/2
  plt.axvline(c)
  plt.axvline(d)
  plt.axvline(e)
  two=itv*(f(a)+4*f(d)+2*f(c)+4*f(e)+f(b))/12
  l+=1
  if l>=max_l:
    return two
  else:
    if abs(two-one)<15*thr:
      return two+(two-one)/15
    else:
      left=adapt_simpson(f,a,c,l,max_l,thr/2,plt)
      right=adapt_simpson(f,c,b,l,max_l,thr/2,plt)
      return left+right

# x=np.linspace(0,1,20)
# y=[f1(v) for v in x]
# plt.plot(x,y)
# print(4*adapt_simpson(f1,0,1,0,4,0.5*10**-5,plt))
# plt.show()

x=np.linspace(0,1/(2**(1/2)),20)
y=[f2(v) for v in x]
plt.plot(x,y)
print(8*adapt_simpson(f2,0,1/(2**(1/2)),0,4,0.5*10**-5,plt))
plt.show()