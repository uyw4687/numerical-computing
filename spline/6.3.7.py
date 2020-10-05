def ev(x):
  for i in range(n-1,-1,-1):
    if x>=t[i]:
      break
  i+=1
  d=a[i+1]*(x-t[i-1])+a[i]*(t[i]-x+h[i+1])/(h[i]+h[i+1])
  e=(a[i]*(x-t[i-1]+h[i-1])+a[i-1]*(t[i-1]-x+h[i]))/(h[i-1]+h[i])
  return (d*(x-t[i-1])+e*(t[i]-x))/h[i]
  
t=[1572,1573,1574,1575,1576,1578,1580,1582,1588,1591,1607]
# t=[1572,1573,1574,1575,1576,1578,1580,1582,1588,1591,1607,1623]
ty=[67259,62280,62350,59250,51457,27603,45435,61162,63455,62164,41471]
# ty=[67259,62280,62350,59250,51457,27603,45435,61162,63455,62164,41471,20778]
n=len(t)-1
h=[t[i]-t[i-1] for i in range(1,len(t))]
h=[h[0],*h]
h.append(h[-1])
d=-1
g=2*ty[0]
p=d*g
q=2
for i in range(1,n+1):
  r=h[i+1]/h[i]
  d*=(-r)
  g=-r*g+(r+1)*ty[i]
  p+=g*d
  q+=(d**2)
a=[(-p/q)]
for i in range(1,n+2):
  a.append(((h[i-1]+h[i])*ty[i-1]-h[i]*a[i-1])/h[i-1])

curr=1572
st=10**-2
res=0
while curr<=1607:
  print(ev(curr))
  res+=ev(curr)*st
  curr+=st
print(res/35)