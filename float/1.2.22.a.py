import numpy as np
import matplotlib.pyplot as plt
from math import e,factorial

x=np.linspace(-1.5,1.5,num=100)

ex,p2x,p3x,r11x,r22x=[[]for j in range(5)]
for xv in x:
  ex.append(e**xv)
  val=1+xv+xv**2/factorial(2)
  p2x.append(val)
  val+=xv**3/factorial(3)
  p3x.append(val)
  r11x.append((1+xv/2)/(1-xv/2))
  r22x.append((1+xv/2+xv**2/12)/(1-xv/2+xv**2/12))
_,(ax1,ax2) = plt.subplots(2)
ax1.plot(x, ex)
ax1.plot(x, p2x,'r')
ax1.plot(x, r11x,'g')
ax2.plot(x, ex)
ax2.plot(x, p3x,'r')
ax2.plot(x, r22x,'g')
plt.show() 