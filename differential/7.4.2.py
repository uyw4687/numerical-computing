t=0
x=3
y=2
h=1/128
n=int(0.38/h)+1

for i in range(n):

  x1=t+x**2-y
  y1=t**2-x+y**2
  x2=1+2*x*x1-y1
  y2=2*t-x1+2*y*y1
  x3=2*x1*x1+2*x*x2-y2
  y3=2-x2+2*y1*y1+2*y*y2

  x=x+h*(x1+1/2*h*(x2+1/3*h*x3))
  y=y+h*(y1+1/2*h*(y2+1/3*h*y3))

  t+=h

  print(t,x,y)
