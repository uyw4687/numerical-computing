from random import random
from math import sqrt

def dist(pa,pb):
  ax,ay,_=pa
  bx,by,_=pb
  return sqrt((bx-ax)**2+(by-ay)**2)

N=10**5

cnt=0
for n in range(N):

  ps=[]
  for i in range(3):
    val=random()
    if val<1/4:
      ps.append((random(),0,'a'))
    elif val<2/4:
      ps.append((random(),1,'b'))
    elif val<3/4:
      ps.append((0,random(),'c'))
    else:
      ps.append((1,random(),'d'))

  pa,pb,pc=ps
  
  a=dist(pb,pc)
  b=dist(pa,pc)
  c=dist(pa,pb)

  if a*b*c==0 or pa[2]==pb[2]==pc[2]:
    continue

  dists=[a,b,c]  
  dists.sort(reverse=True)

  if b**2+c**2-a**2 < 0:
    cnt+=1

print(cnt/N)