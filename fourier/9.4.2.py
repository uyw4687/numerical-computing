from math import pi,e
import numpy as np

i=complex(0,1)

dets=[]
for n in range(2,16):
  tot=0
  totsq=0
  prod=1
  ws=[]
  for k in range(1,n+1):
    rk=e**(i*2*pi*k/n)
    # print(f"omega({k})",rk)
    # print(f"omega({k})**{n}", rk**n)

    tot+=rk
    totsq+=(rk**2)
    prod*=rk
    ws.append(rk)

  # print("sum",tot)
  # print("sum of squares",totsq)
  # print("product",prod)

  ws=[ws[n-1]]+ws[:n-1]

  mat=[]
  for ii in range(n):
    mid=[]
    for jj in range(n):
      mid.append(ws[ii*jj%n])
    mat.append(mid)

  det=np.linalg.det(mat)
  print("n",n,"det",det)
  dets.append(det)

for i in range(len(dets)-1):
  print(dets[i+1]/dets[i])
  print()