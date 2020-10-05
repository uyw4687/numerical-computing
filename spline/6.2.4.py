def f(x):
  # return (x+1)
  return 1/(x**2+1)
def S(x):
  if x<t[0] or x>t[n]:
    print("out of bound")
    return None
  for i in range(n):
    if x<=t[i+1]:
      break
  val=z[i]/2+(x-t[i])*(z[i+1]-z[i])/6/h[i]
  val=B[i]+(x-t[i])*val
  val=ty[i]+(x-t[i])*val
  return val

# n=4
n=40
# t=[(4*i/n) for i in range(n+1)]
t=[(-5+10*i/n) for i in range(n+1)]
ty=[f(x) for x in t]
h=[(t[i+1]-t[i]) for i in range(len(t)-1)]
b=[((ty[i+1]-ty[i])/h[i]) for i in range(len(ty)-1)]
u=[None,2*(h[0]+h[1])]
v=[None,6*(b[1]-b[0])]
for i in range(2,len(h)):
  u.append(2*(h[i-1]+h[i])-(h[i-1]**2)/u[i-1])
  v.append(6*(b[i]-b[i-1])-(h[i-1]*v[i-1])/u[i-1])
z=[0]*(n+1)
for i in range(n-1,0,-1):
  z[i]=(v[i]-h[i]*z[i+1])/u[i]

B=[(-h[i]*z[i+1]/6-h[i]*z[i]/3+(ty[i+1]-ty[i])/h[i]) for i in range(len(ty)-1)]

# for i in range(-1,10):
#   print(S(i))
curr=0
for i in range(101):
  print(S(curr)-f(curr))
  curr+=5/100