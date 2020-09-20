n=4
x=[1,2,3,-4,5]
a=[2,48,272,1182,2262]
for j in range(1,n+1):
  for i in range(n,j-1,-1):
    a[i]=(a[i]-a[i-1])/(x[i]-x[i-j])
print(a)

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
print(p)

temp=a[n]
t=-1
for i in range(n-1,-1,-1):
  temp=temp*(t-x[i])+a[i]
print(temp)