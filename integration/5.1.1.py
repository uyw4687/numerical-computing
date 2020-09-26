def f(v):
  return (v**2+1)**(-1)

def trap_uni(f,a,b,n):
  h=(b-a)/n
  x=[a+h*i for i in range(n+1)]
  y=[f(v) for v in x]
  total=0
  for i in range(n):
    total+=(h*(y[i]+y[i+1])/2)
  return total

print(trap_uni(f,0,1,2))