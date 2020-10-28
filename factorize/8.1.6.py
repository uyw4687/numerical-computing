N=10

a=[[0]*N for i in range(N)]

for i in range(N):

  if i!=0:
    a[i][i-1]=1
  if i!=N-1:
    a[i][i+1]=1
  a[i][i]=-2

mul=[]

for i in range(N-1): # row

  m=a[i+1][i]/a[i][i]
  print(m)
  mul.append(m)

  a[i+1][i+1]-=(a[i][i+1]*m)

for r in a:
  print(r)
print()

B=[]

for i in range(N):
  b=[0]*N
  b[i]=1

  for j in range(i,N-1):
    b[j+1]-=(b[j]*mul[j])

  b[N-1]=b[N-1]/a[N-1][N-1]

  for j in range(N-2,-1,-1):
    b[j]=(b[j]-a[j][j+1]*b[j+1])/a[j][j]
  
  B.append(b)
  print(b)

print()
  

c=[[0]*N for i in range(N)]
for i in range(N):
  for j in range(i,N):
    c[i][j] = -(i+1)*(N+1-(j+1))/(N+1)
    c[j][i] = -(i+1)*(N+1-(j+1))/(N+1)

for r in c:
  print(r)
print()

# for i in range(N):
#   for j in range(N):
#     print(abs((B[i][j]-c[i][j])/B[i][j]))