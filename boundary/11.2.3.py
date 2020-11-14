from math import cos,pi,sin

def u(t):
  return -2*t*cos(t)+t

def v(t):
  return -1

def w(t):
  return t

tz=0
tn=pi

n=10
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

mat[0][n-1]=b(h)
for r in range(1,n-2):
  ti=h*(r+1)
  mat[r][n-1]=b(ti)
mat[n-2][n-1]=b(h*(n-1))-c(h*(n-1))*pi

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

print(sol)

print([(pi/10*t)+2*sin((pi/10*t)) for t in range(11)])