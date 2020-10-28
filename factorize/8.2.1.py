import numpy as np
from math import cos,pi

a=np.array([[1,7],[2,-5]])
# c,d=np.linalg.eig(a)
# print(c)
# print(d)
# print()

a=np.array([[4,-7,3,2,3],
[1,6,11,-1,2],
[5,-5,-2,-4,1],
[9,-3,1,6,5],
[3,2,5,-5,1]
])
# c,d=np.linalg.eig(a)
# print(c)
# print(d)

a=[[0]*12 for i in range(12)]
for i in range(1,13):
  for j in range(1,13):
    if i<=j:
      a[i-1][j-1]=i/j
    else:
      a[i-1][j-1]=j/i

# c,d=np.linalg.eig(a)
# print(c)
# print(d)

for N in range(5,21):
  a=[[0]*N for j in range(N)]
  for j in range(N):
    if j!=0:
      a[j][j-1]=-1
    if j!=N-1:
      a[j][j+1]=-1
    a[j][j]=2

  # c,_=np.linalg.eig(a)
  # print(c)
  # print("-> ",[2-2*cos(j*pi/(N+1)) for j in range(1,N+1)])


N=30
a=[[0]*N for j in range(N)]
for i in range(N):
  for j in range(i,N):
    a[i][j]=N-j
    a[j][i]=N-j

c,_=np.linalg.eig(a)
print(c)
print("-> ",[1/(2-2*cos((2*i-1)*pi/(2*N+1))) for i in range(1,N+1)])
