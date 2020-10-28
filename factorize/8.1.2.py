N=4

a=[[5,7,6,5],
[7,10,8,7],
[6,8,10,9],
[5,7,9,10]]
l=[[0]*N for i in range(N)]
u=[[0]*N for i in range(N)]

# #Doolittle
# for i in range(N):

#   u[i][i]=1

#   for j in range(i,N):
#     total=0
#     for k in range(i):
#       total+=(l[j][k]*u[k][i])
#     l[j][i]=(a[j][i]-total)/u[i][i]

#   for j in range(i,N):
#     total=0
#     for k in range(i):
#       total+=(l[i][k]*u[k][j])
#     u[i][j]=(a[i][j]-total)/l[i][i]

# #Crout
# for i in range(N):

#   l[i][i]=1

#   for j in range(i,N):
#     total=0
#     for k in range(i):
#       total+=(l[i][k]*u[k][j])
#     u[i][j]=(a[i][j]-total)/l[i][i]

#   for j in range(i,N):
#     total=0
#     for k in range(i):
#       total+=(l[j][k]*u[k][i])
#     l[j][i]=(a[j][i]-total)/u[i][i]

# dl=[1,None,1,None]
# du=[None,1,None,1]
# dl=[None,1,None,1]
# du=[1,None,1,None]
dl=[None,None,7,9]
du=[3,5,None,None]
# dl=[None]*4
# du=[3,5,0.285714857142852,0.05555555555555496]

#Generalization
for i in range(N):

  if dl[i]!=None:
    l[i][i]=dl[i]

    for j in range(i,N):
      total=0
      for k in range(i):
        total+=(l[i][k]*u[k][j])
      u[i][j]=(a[i][j]-total)/l[i][i]

    for j in range(i,N):
      total=0
      for k in range(i):
        total+=(l[j][k]*u[k][i])
      l[j][i]=(a[j][i]-total)/u[i][i]

  else:
    u[i][i]=du[i]

    for j in range(i,N):
      total=0
      for k in range(i):
        total+=(l[j][k]*u[k][i])
      l[j][i]=(a[j][i]-total)/u[i][i]

    for j in range(i,N):
      total=0
      for k in range(i):
        total+=(l[i][k]*u[k][j])
      u[i][j]=(a[i][j]-total)/l[i][i]

for r in l:
  print(r)
print()

for r in u:
  print(r)
print()

import numpy as np

l= np.asarray(l)
u= np.asarray(u)

for r in l.dot(u):
  print(r)
