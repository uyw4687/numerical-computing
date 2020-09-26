from math import sin,pi,e,atan,log
def f1(v):
  return sin(v)
def f2(v):
  return e**v
def f3(v):
  return atan(v)
def integ_f3(v):
  return v*atan(v)-log(1+v**2)/2

def trap_uni(f,a,b,n):
  h=(b-a)/n
  x=[a+h*i for i in range(n+1)]
  y=[f(v) for v in x]
  total=0
  for i in range(n):
    total+=(h*(y[i]+y[i+1])/2)
  return total

res1=trap_uni(f1,0,pi,15)
rv1=2
print(res1)
print(rv1)
print(abs((res1-rv1)/rv1)*100,end='%\n\n')

res2=trap_uni(f2,0,1,5)
rv2=e-1
print(res2)
print(rv2)
print(abs((res2-rv2)/rv2)*100,end='%\n\n')

res3=trap_uni(f3,0,1,5)
rv3=integ_f3(1)-integ_f3(0)
print(res3)
print(rv3)
print(abs((res3-rv3)/rv3)*100,end='%\n\n')