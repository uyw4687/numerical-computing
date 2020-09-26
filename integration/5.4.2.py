from math import cos,e
def f(x):
  return x**(-1/2)
def g(x):
  return e**(-(cos(x))**2)
def trans(t,a,b):
  return (b-a)/2*t+(b+a)/2

a=0
b=1
left=5/9*f(trans(-(3/5)**(1/2),a,b))
mid=8/9*f((a+b)/2)
right=5/9*f(trans((3/5)**(1/2),a,b))
print((b-a)/2*(left+mid+right))

a=0
b=2
left=5/9*g(trans(-(3/5)**(1/2),a,b))
mid=8/9*g((a+b)/2)
right=5/9*g(trans((3/5)**(1/2),a,b))
print((b-a)/2*(left+mid+right))