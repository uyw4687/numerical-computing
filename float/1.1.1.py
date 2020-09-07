from math import sin,cos
x=0.5
n=30
h=1
emax=0
for i in range(n):
  h*=0.25
  y=(sin(x+h)-sin(x))/h
  error=abs(cos(x)-y)
  print(i,"/",h,"/",y,"/",error)
  if error>emax:
    emax=error
    imax=i
print(imax,emax)
