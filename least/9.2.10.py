import numpy as np
from matplotlib import pyplot as plt

x=[-1,-1/2,0,1/2,1]
y=[-1,0,1,2,1]
plt.plot(x,y,'o')

fs=[]
fs.append(lambda x:1)
fs.append(lambda x:x)
fs.append(lambda x:2*x**2-1)

a=np.zeros((len(x),len(fs)))
h,w=a.shape

for j in range(w):
  cf = fs[j]
  for i in range(h):
    a[i][j]=cf(x[i])

cs,_,_,_=np.linalg.lstsq(a,y,rcond=None)
print(cs)

x=np.linspace(-1,1,51)
y=cs[0]+cs[1]*x+cs[2]*(2*x*x-1)
plt.plot(x,y)
plt.show()

#gauss
import numpy as np
from matplotlib import pyplot as plt
x=[-1,-1/2,0,1/2,1]
y=[-1,0,1,2,1]
plt.plot(x,y,'o')

fs=[]
fs.append(lambda x:1)
fs.append(lambda x:x)
fs.append(lambda x:2*x**2-1)

n=len(fs)
m=len(x)
b=[]

for i in range(n):
  v=0
  cf=fs[i]
  for j in range(m):
    v+=y[j]*cf(x[j])
  b.append(v)

a=np.zeros((n,n))
for i in range(n):
  for j in range(i,n):
    v=0
    cfl,cfr=fs[i],fs[j]
    for k in range(m):
      v+=cfl(x[k])*cfr(x[k])
    a[i][j]=v
    a[j][i]=v

for r in a:
  print(r)

from copy import deepcopy
mat=a
origmat=deepcopy(mat)
origb=deepcopy(b)

for k in range(n-1):
  for i in range(k+1,n):
    rat=mat[i][k]/mat[k][k]
    for j in range(k+1,n):
      mat[i][j]-=rat*mat[k][j]
    b[i]-=rat*b[k]

cs=[]
for k in range(n-1,-1,-1):
  v=b[k]
  for i in range((n-1)-k):
    v-=cs[i]*mat[k][n-1-i]
  cs.append(v/mat[k][k])
cs=cs[::-1]
print('cs',cs)
print()

x=np.linspace(-1,1,51)
y=cs[0]+cs[1]*x+cs[2]*(2*x*x-1)
plt.plot(x,y)
plt.show()