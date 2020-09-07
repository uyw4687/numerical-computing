from math import log
x=1
s=1
for i in range(5000):
  x+=1
  s+=1/x
  if i%100==0:
    print('i',i)
    print('s',s)
    print('ec',s-log(x))