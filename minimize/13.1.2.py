from math import sin,sqrt,pi

f=sin

eb=10**-10

r=-1/2+sqrt(5)/2

a=0
b=pi/2
iv=b-a
c=a+iv*r
d=a+iv*r*r
fc=f(c)
fd=f(d)

for i in range(100):
  if fc<fd:
    a=d
    iv=b-a

    d=c
    fd=fc
    c=a+iv*r
    fc=f(c)
  else:
    b=c
    iv=b-a

    c=d
    fc=fd
    d=a+iv*r*r
    fd=f(d)
  if (b-a)/2<eb:
    break
print(a,b)
print(i)