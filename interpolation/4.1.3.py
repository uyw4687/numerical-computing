from math import e
from random import random
n=10
x=[random()*2 for i in range(11)]
a=[e**v for v in x]
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

t=[random()*2 for i in range(100)]
temp=[a[n] for i in range(len(t))]
for j in range(len(t)):
  for i in range(n-1,-1,-1):
    temp[j]=temp[j]*(t[j]-x[i])+a[i]
# print(t)
# print(temp)
real=[e**v for v in t]
# print(real)
errpcnt = [abs((real[i]-temp[i])/real[i])*100 for i in range(len(t))]
# print(errpcnt)
print(min(errpcnt))
print(max(errpcnt))
print(sum(errpcnt)/len(t))