import numpy as np
import matplotlib.pyplot as plt
from math import e,factorial

x=np.linspace(-1.5,1.5,num=100)

ex,p2x,p3x,p4x,p5x=[[]for j in range(5)]
for xv in x:
  ex.append(e**xv)
  val=1+xv+xv**2/factorial(2)
  p2x.append(val)
  val+=xv**3/factorial(3)
  p3x.append(val)
  val+=xv**4/factorial(4)
  p4x.append(val)
  val+=xv**5/factorial(5)
  p5x.append(val)
_,(ax1,ax2,ax3,ax4) = plt.subplots(4)
ax1.plot(x, ex)
ax1.plot(x, p2x,'r')
ax2.plot(x, ex)
ax2.plot(x, p3x,'r')
ax3.plot(x, ex)
ax3.plot(x, p3x,'r')
ax4.plot(x, ex)
ax4.plot(x, p3x,'r')
plt.show() 