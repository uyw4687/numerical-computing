import numpy as np

a=np.asarray([[5,4,1,1],
[4,5,1,1],
[1,1,4,2],
[1,1,2,4]], dtype=np.float64)
c,d=np.linalg.eig(a)
print(c)
print(d)
print()

x=np.asarray([1,1,1,1])
s=0
rs=[]
for i in range(15):
  y=a.dot(x)
  r=y[0]/x[0]
  rs.append(r)
  x=y/np.abs(y).max()
  if i>4:
    s=rs[i]-((rs[i]-rs[i-1])**2)/(rs[i]-2*rs[i-1]+rs[i-2])
  print(x,'r',r,'s',s)
print()

ainv=np.linalg.inv(a)

x=np.asarray([1,1,1,1])
for i in range(70):
  y=ainv.dot(x)
  r=y[0]/x[0]
  x=y/np.abs(y).max()
  print(x,r)
print()

# b=np.asarray(a)
# for i in range(4):
#   b[i][i]-=2.1
# print(b)
# c,_=np.linalg.eig(b)
# print(c)
# print()

# binv=np.linalg.inv(b)
# x=np.asarray([1,1,1,1])
# for i in range(50):
#   y=binv.dot(x)
#   r=y[0]/x[0]
#   x=y/np.abs(y).max()
#   print(x,r)
# print()

# b=np.asarray(a)
# for i in range(4):
#   b[i][i]-=5.1
# print(b)
# c,_=np.linalg.eig(b)
# print(c)
# print()

# binv=np.linalg.inv(b)
# x=np.asarray([1,1,1,1])
# for i in range(20):
#   y=binv.dot(x)
#   r=y[0]/x[0]
#   x=y/np.abs(y).max()
#   print(x,r)
# print()
