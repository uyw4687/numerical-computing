h=2**-4
k=2**-10
sigma = k/h**2

nx=2**4+1

xs=[h*i for i in range(nx)]
us=[xv*(1-xv) for xv in xs]
print(us)
print()

for i in range(128):

  nus=[0]*nx
  
  for j in range(1,nx-1):
    nus[j] = sigma*(us[j-1]+us[j+1])+(1-2*sigma)*us[j]
  
  print(nus)
  print()
  us=nus
