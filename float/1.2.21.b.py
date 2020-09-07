import numpy as np
import matplotlib.pyplot as plt
from math import log

x=np.linspace(-0.75,1,num=100)

lnx,p2x,p3x,p4x,p5x=[[]for j in range(5)]
for xv in x:
  lnx.append(log(1+xv))
  val=xv-xv**2/2
  p2x.append(val)
  val+=xv**3/3
  p3x.append(val)
  val-=xv**4/4
  p4x.append(val)
  val+=xv**5/5
  p5x.append(val)
_,(ax1,ax2,ax3,ax4) = plt.subplots(4)
ax1.plot(x, lnx)
ax1.plot(x, p2x,'r')
ax2.plot(x, lnx)
ax2.plot(x, p3x,'r')
ax3.plot(x, lnx)
ax3.plot(x, p3x,'r')
ax4.plot(x, lnx)
ax4.plot(x, p3x,'r')
plt.show() 