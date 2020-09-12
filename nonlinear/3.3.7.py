def f(x):
  return x**3+2*x**2+10*x-20

x=[2,1]
i=1
while True:
  if abs(x[-1]-x[-2]) < 10**-15:
    break
  x.append(x[i]-(x[i]-x[i-1])/(f(x[i])-f(x[i-1]))*f(x[i]))
  print(x[-1])
  i+=1

def fd(x):
  return 3*x**2+4*x+10

print()
x=1
while True:
  err=f(x)/fd(x)
  if abs(err) < 10**-15:
    break
  x=x-err
  print(x)
