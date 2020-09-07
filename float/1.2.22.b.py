import numpy as np
import matplotlib.pyplot as plt
from math import log

x=np.linspace(-0.75,1,num=100)

lnx,p2x,p3x,r22x,r31x=[[]for j in range(5)]
for xv in x:
  lnx.append(log(1+xv))
  val=xv-xv**2/2
  p2x.append(val)
  val+=xv**3/3
  p3x.append(val)
  r22x.append((xv+xv**2/2)/(1+xv+xv**2/6))
  r31x.append((xv+xv**2/4-xv**3/24)/(1+xv*3/4))
_,(ax1,ax2) = plt.subplots(2)
ax1.plot(x, lnx)
ax1.plot(x, p2x,'r')
ax1.plot(x, r22x,'g')
ax2.plot(x, lnx)
ax2.plot(x, p3x,'r')
ax2.plot(x, r31x,'g')
plt.show() 