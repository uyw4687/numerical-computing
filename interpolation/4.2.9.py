n=10
x=[-1+i*(2/n) for i in range(n+1)]
# from math import cos,pi
# aa,bb=-1,1
# x=[(aa+bb)/2+(bb-aa)/2*cos(pi*(2*i+1)/(2*n+2)) for i in range(n+1)]
a=[abs(v) for v in x]
for j in range(1,n+1):
  for i in range(n,j-1,-1):
    a[i]=(a[i]-a[i-1])/(x[i]-x[i-j])
# print(x)
# print(a)

p=''
for i in range(n+1):
  p+=str(a[i])
  for j in range(i):
    if x[j]>=0:
      p+='(x-'+str(x[j])+')'
    else:
      p+='(x+'+str(-x[j])+')'
  if i!=n:
    p+='+'
# print(p)

t=[-1+i*(2/40) for i in range(41)]
temp=[a[n] for i in range(len(t))]
for j in range(len(t)):
  for i in range(n-1,-1,-1):
    temp[j]=temp[j]*(t[j]-x[i])+a[i]
print(t)
print(temp)
real=[abs(v) for v in t]
print(real)
err = [real[i]-temp[i] for i in range(len(t))]
print(err)
print(min([abs(v) for v in err]))
print(max([abs(v) for v in err]))