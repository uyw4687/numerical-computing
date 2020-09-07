n=10
mat=[]
b=[]
for i in range(1,n+1):
  r=[1/(i+j-1) for j in range(1,n+1)]
  mat.append(r)
  b.append(sum(r))
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

for lv in l:
  print(mat[lv])

x=[]
for k in range(n-1,-1,-1):
  v=b[l[k]]
  for i in range((n-1)-k):
    v-=x[i]*mat[l[k]][n-1-i]
  x.append(v/mat[l[k]][k])
x=x[::-1]
print('x',x)