n=30
d=5
c=-1
ratios=[]
ds=[d]
temp=d
for i in range(n-1):
  ratio=c/temp
  ratios.append(ratio)
  temp=d-c*ratio
  ds.append(temp)

b=list(range(1,n+1))
for i in range(n-1):
  b[i+1]-=b[i]*ratios[i]

b[n-1]/=ds[n-1]
for i in range(n-2,-1,-1):
  b[i]=(b[i]-c*b[i+1])/ds[i]
print(b)

print(d*b[0]+c*b[1])
for i in range(0,n-2):
  print(c*b[i]+d*b[i+1]+c*b[i+2])
print(c*b[n-2]+d*b[n-1])
