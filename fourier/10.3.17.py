from random import random

N=10**5

cnt=0
for _ in range(N):
  
  curr=[0,0]
  for _ in range(50):
    val=random()
    if val<1/4:
      curr[1]+=1
    elif val<1/4+1/4:
      curr[1]-=1
    elif val<1/4+1/4+1/3:
      curr[0]-=1
    else:
      curr[0]+=1
  
  if curr[0]**2+curr[1]**2 >= 20**2:
    cnt+=1

print(cnt/N)
