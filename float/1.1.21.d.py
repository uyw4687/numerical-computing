radius=1
area=22/7*radius**2
circum=2*3.1416*radius
print('area',area)
print('circum',circum)

from math import pi
print("<with math.pi>")
area2=pi*radius**2
circum2=2*pi*radius
print('area',area2)
print('circum',circum2)
print()
print("relative error")
print(abs((area2-area)/area2)*100,end='%\n')
print(abs((circum2-circum)/circum2),end='%\n')