from math import e

# h=0.1
# h=0.2
# h=0.25
# h=0.05
h=0.25
xs=-1
xe=1
ys=-1.5
ye=1.5

nx=round((xe-xs)/h+1)
ny=round((ye-ys)/h+1)
vxs=[xs+h*i for i in range(nx)]
vys=[ys+h*i for i in range(ny)]
vs=[[0]*nx for i in range(ny)]
for i in range(1,ny-1):
  for j in range(1,nx-1):
    # vs[i][j]=vys[i]*vxs[j]
    # vs[i][j]=0
    # vs[i][j]=(1+vys[i])*(1+vxs[j])
    # vs[i][j]=(1+vys[i]+0.5*vys[i]**2)*(1+vxs[j]+0.5*vxs[j]**2)
    vs[i][j]=1+vys[i]*vxs[j]
for i in range(nx):
  vs[0][i]=e**(vxs[i]+ys)
  vs[ny-1][i]=e**(vxs[i]+ye)
for i in range(ny):
  vs[i][0]=e**(xs+vys[i])
  vs[i][nx-1]=e**(xe+vys[i])

def g(a,b):
  return 2*e**(a+b)

# nit=15
# nit=20
# nit=40
# nit=100
nit=200
for _ in range(nit):

  for i in range(1,ny-1):
    for j in range(1,nx-1):
      vs[i][j]=(vs[i+1][j]+vs[i-1][j]+vs[i][j+1]+vs[i][j-1]-h**2*g(vys[i],vxs[j]))/4

for x in vs:
  print(x)
print()

for i in range(ny):
  for j in range(nx):
    rv=e**(vys[i]+vxs[j])
    print((vs[i][j]-rv)/rv*100, end="% ")
  print()