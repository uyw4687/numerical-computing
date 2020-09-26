from math import sin
def f(x):
  return sin(x)/x

n=7

a=1.3
b=2.19
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