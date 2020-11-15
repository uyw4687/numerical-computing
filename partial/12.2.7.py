h=0.1
k=0.05
rho=k**2/h**2

nx=20+1

ni=20

xs=[-1+h*i for i in range(nx)]
us=[abs(v)-1 for v in xs]

nus=[0]*nx
for i in range(1,nx-1):
  nus[i]=rho/2*(us[i+1]+us[i-1])+(1-rho)*us[i]

for i in range(ni-1):
  nnus=[0]*nx
  for i in range(1,nx-1):
    nnus[i]=rho*(nus[i+1]+nus[i-1])+2*(1-rho)*nus[i]-us[i]

  us=nus
  nus=nnus
