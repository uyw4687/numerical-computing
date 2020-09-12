from random import random
x=2*random()
for i in range(100):
  if x<0.5:
    x=2*x
  else:
    x=2*x-1
  print(x)
