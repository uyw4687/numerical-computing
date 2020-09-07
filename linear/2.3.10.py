n=7
d=[24,13,15,4,35,13,24]
a=[12,34,14,4,15,43,23]
b=[12,23,42,51,33,24,15]

#gauss
for i in range(n//2):
  rat=a[i]/d[i]
  d[n-1-i]-=a[n-1-i]*rat
  b[n-1-i]-=b[i]*rat

#solve
for i in range(n-1,n//2-1,-1):
  b[i]/=d[i]
for i in range(n//2-1,-1,-1):
  b[i]=(b[i]-a[n-1-i]*b[n-1-i])/d[i]

print(b)
d=[24,13,15,4,35,13,24]
a=[12,34,14,4,15,43,23]

for i in range(n//2):
  print(d[i]*b[i]+a[n-1-i]*b[n-1-i])
print(d[n//2]*b[n//2])
for i in range(n//2+1,n):
  print(d[i]*b[i]+a[n-1-i]*b[n-1-i])