from math import sin
def f(x):
  return 2*sin(x**2)

n=7

a=0
b=1
h=b-a
d=h*(f(a)+f(b))/2
rom=[[0]*(n+1) for i in range(n+1)]
rom[0][0]=d

for i in range(1,n+1):
  rom[i][0]=rom[i-1][0]/2
  h/=2
  for j in range(2**(i-1)):
    rom[i][0]+=(h*f(a+(2*j+1)*h))
  for j in range(1,i+1):
    rom[i][j]=rom[i][j-1]+(rom[i][j-1]-rom[i-1][j-1])/(4**j-1)

for i,r in enumerate(rom):
  print(r[:i+1])