N=4

a=[[7,3,-1,2],
[3,8,1,-4],
[-1,1,4,-1],
[2,-4,-1,6]]
b=[-1,0,-3,1]

# x=[0]*N

# #Jacobi
# for t in range(80):
#   y=[0]*N
#   for i in range(N):
#     total=0
#     for j in range(N):
#       if i!=j:
#         total+=x[j]*a[i][j]
#     y[i]=(b[i]-total)/a[i][i]
#   print(t+1,y)
#   x=y

# x=[0]*N

# #Gauss-Seidel
# for t in range(50):
#   for i in range(N):
#     total=0
#     for j in range(N):
#       if i!=j:
#         total+=x[j]*a[i][j]
#     x[i]=(b[i]-total)/a[i][i]
#   print(t+1,x)

x=[0]*N
w=1.4

#SOR
for t in range(20):
  for i in range(N):
    total=0
    for j in range(N):
      if i!=j:
        total+=x[j]*a[i][j]
    x[i]=w*(b[i]-total)/a[i][i]+(1-w)*x[i]
  print(t+1,x)
