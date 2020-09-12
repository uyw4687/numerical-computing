def f(x):
  res=1
  for i in range(1,21):
    res*=(x-i)
  return res-(10**(-8))*x**19

x=[20,21]
i=1
while True:
  if abs(x[-1]-x[-2]) < 10**-15:
    break
  x.append(x[i]-(x[i]-x[i-1])/(f(x[i])-f(x[i-1]))*f(x[i]))
  print(x[-1])
  i+=1