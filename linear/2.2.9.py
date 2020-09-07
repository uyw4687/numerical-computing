#scaled
from copy import deepcopy
n=4
b=[9.5740,7.2190,5.7300,6.2910]
mat=[
  [0.0001,-5.0300,5.8090,7.8320],
  [2.2660,1.9950,1.2120,8.0080],
  [8.8500,5.6810,4.5520,1.3020],
  [6.7750,-2.2530,2.9080,3.9700]
]
origmat=deepcopy(mat)
origb=deepcopy(b)
s=[max([abs(x) for x in mat[i]]) for i in range(n)]
l=list(range(n))

for k in range(n-1):
  rmax=0
  rmaxind=0
  for i in range(k,n):
    if abs(mat[l[i]][k]/s[l[i]])>rmax:
      rmax=mat[l[i]][k]
      rmaxind=i
  l[rmaxind],l[k]=l[k],l[rmaxind]
  for i in range(k+1,n):
    rat=mat[l[i]][k]/mat[l[k]][k]
    # mat[l[i]][k]=rat
    for j in range(k+1,n):
      mat[l[i]][j]-=rat*mat[l[k]][j]
    b[l[i]]-=rat*b[l[k]]

# for lv in l:
#   print(mat[lv])

x=[]
for k in range(n-1,-1,-1):
  v=b[l[k]]
  for i in range((n-1)-k):
    v-=x[i]*mat[l[k]][n-1-i]
  x.append(v/mat[l[k]][k])
x=x[::-1]
print('x',x)
print()

for i in range(n):
  res=0
  for j in range(n):
    res+=origmat[i][j]*x[j]
  # print(res)
  print(100*abs((res-origb[i])/origb[i]),end='%\n')
print()

#naive
from copy import deepcopy
n=4
b=[9.5740,7.2190,5.7300,6.2910]
mat=[
  [0.0001,-5.0300,5.8090,7.8320],
  [2.2660,1.9950,1.2120,8.0080],
  [8.8500,5.6810,4.5520,1.3020],
  [6.7750,-2.2530,2.9080,3.9700]
]
origmat=deepcopy(mat)
origb=deepcopy(b)

for k in range(n-1):
  for i in range(k+1,n):
    rat=mat[i][k]/mat[k][k]
    for j in range(k+1,n):
      mat[i][j]-=rat*mat[k][j]
    b[i]-=rat*b[k]

# for lv in l:
#   print(mat[lv])

x=[]
for k in range(n-1,-1,-1):
  v=b[k]
  for i in range((n-1)-k):
    v-=x[i]*mat[k][n-1-i]
  x.append(v/mat[k][k])
x=x[::-1]
print('x',x)
print()

for i in range(n):
  res=0
  for j in range(n):
    res+=origmat[i][j]*x[j]
  # print(res)
  print(100*abs((res-origb[i])/origb[i]),end='%\n')