from math import pi,tan,log
for n in range(1,101):
  sig=0
  for k in range(1,n+1):
    sig+=tan(pi*k/(2*n+1))/k
  pn=1/(2*n+1)+2/pi*sig
  print(pn,4/pi**2*log(2*n+1)+1-pn)
  