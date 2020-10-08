from math import sqrt
def f(t,x):
  return sqrt(1+t**3)
curr=0
res=0
h=0.1
while curr+h<=1:
  k1=h*f(curr,res)
  k2=h*f(curr+h/2,res+k1/2)
  k3=h*f(curr+h/2,res+k2/2)
  k4=h*f(curr+h,res+k3)
  res=res+(k1+2*k2+2*k3+k4)/6
  curr+=h
  print("t",curr,"x",res)