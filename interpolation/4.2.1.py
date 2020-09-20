n=20
x=[-5+i*(10/20) for i in range(21)]
a=[1/(v**2+1) for v in x]
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

t=[-5+i*(10/40) for i in range(41)]
temp=[a[n] for i in range(41)]
for j in range(len(t)):
  for i in range(n-1,-1,-1):
    temp[j]=temp[j]*(t[j]-x[i])+a[i]
print(t)
print(temp)
real=[1/(v**2+1) for v in t]
print(real)
errpcnt = [abs((real[i]-temp[i])/real[i])*100 for i in range(len(t))]
print(errpcnt)
print(min(errpcnt))
print(max(errpcnt))
print(sum(errpcnt)/len(t))