# for x2 in range(0,20,1):
#   t=0
#   x1=40
#   n=100
#   h=10/n

#   print(x2)
#   for i in range(n):

#     x1p=x2
#     x2p=0.01*x1-0.2

#     x1=x1+h*x1p
#     x2=x2+h*x2p

#     t+=h

#   print(t,x1,x2)

# t=0
# x1=40
# x2=13
# n=10
# h=10/n

from math import e
def an(t):
  c1=(180-20/e)/(e-1/e)
  c2=20-c1
  return c1*e**(0.1*t)+c2*e**(-0.1*t)+20

# for i in range(n):

#   x1p=x2
#   x2p=0.01*x1-0.2

#   x1=x1+h*x1p
#   x2=x2+h*x2p

#   t+=h
#   print(t,x1,an(t))

def u(t):
  return -0.2

def v(t):
  return 0.01

def w(t):
  return 0

tz=0
tn=10

n=5
h=(tn-tz)/n

mat=[[0]*(n-1 +1) for i in range(n-1)]

def a(t):
  return -(1+h/2*w(t))

def d(t):
  return 2+v(t)*h**2

def c(t):
  return -(1-h/2*w(t))

def b(t):
  return -u(t)*h**2

mat[0][0]=d(h)
mat[0][1]=c(h)
for i in range(1,n-2):
  ti=h*(i+1)
  mat[i][i-1]=a(ti)
  mat[i][i]=d(ti)
  mat[i][i+1]=c(ti)
mat[n-2][n-3]=a(h*(n-1))
mat[n-2][n-2]=d(h*(n-1))

mat[0][n-1]=b(h)-a(h)*40
for r in range(1,n-2):
  ti=h*(r+1)
  mat[r][n-1]=b(ti)
mat[n-2][n-1]=b(h*(n-1))-c(h*(n-1))*200

for r in mat:
  print(r)
print()

for r in range(n-2):
  rat = mat[r+1][r]/mat[r][r]
  for j in range(n):
    mat[r+1][j]-=rat*mat[r][j]

for r in mat:
  print(r)
print()

for r in range(n-2,-1,-1):
  rat = mat[r-1][r]/mat[r][r]
  for j in range(n):
    mat[r-1][j]-=rat*mat[r][j]

for r in mat:
  print(r)
print()

sol=[0]*(n-1)
for i in range(n-1):
  sol[i] = mat[i][n-1]/mat[i][i]

for i,v in enumerate(sol):
  t=h*(i+1)
  print(t,v,an(t))