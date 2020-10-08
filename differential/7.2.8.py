from math import e
def f(t,x):
  if t<=0:
    return x+t
  else:
    return x-t

def x(t):
  if t<=0:
    return e**(t+1)-(t+1)
  else:
    return e**(t+1)-2*e**t+(t+1)

curr=-1
res=1
# h=0.09
h=0.1
while curr+h<=1:
  k1=h*f(curr,res)
  k2=h*f(curr+h/2,res+k1/2)
  k3=h*f(curr+h/2,res+k2/2)
  k4=h*f(curr+h,res+k3)
  res=res+(k1+2*k2+2*k3+k4)/6
  curr+=h
  print("t",curr,"x",res)
  print("r", x(curr), "e", x(curr)-res, "pe", abs((x(curr)-res)/x(curr))*100)