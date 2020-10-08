def x(t):
  return t**3-9*t**2/2+13*t/2
def f(t,x):
  return 3*x/t+9*t/2-13

hmin=1/20
hmax=2
n=10
emin=10**-10
emax=10**-5
t=a=3
b=1/2
h=(b-a)/n
res=6

while True:
  k1=h*f(t,res)
  k2=h*f(t+h/4,res+k1/4)
  k3=h*f(t+3*h/8,res+3*k1/32+9*k2/32)
  k4=h*f(t+12*h/13,res+1932*k1/2197-7200*k2/2197+7296*k3/2197)
  k5=h*f(t+h,res+439*k1/216-8*k2+3680*k3/513-845*k4/4104)
  k6=h*f(t+h/2,res-8*k1/27+2*k2-3544*k3/2565+1859*k4/4104-11*k5/40)
  x4=res+25*k1/216+1408*k3/2565+2197*k4/4104-k5/5
  res+=(16*k1/135+6656*k3/12825+28561*k4/56430-9*k5/50+2*k6/55)
  t+=h
  print("t",t,"x",res)
  print("r",x(t),"e",x(t)-res,"pe",(x(t)-res)/x(t)*100)
  if abs(t-b)<emin:
    break
  if abs(res-x4)<emin:
    h*=2
  elif abs(res-x4)>emax:
    h/=2
  
  if abs(h)<hmin:
    h=hmin if h>=0 else -hmin
  elif abs(h)>hmax:
    h=hmax if h>=0 else -hmax
  if b<t:
    if t+h<b:
      h=b-t
  else:
    if t+h>b:
      h=b-t