from math import sqrt,atan
x=1
for n in range(3,21):
  x=x/sqrt(2*(1+sqrt(1-x**2)))
  print("<n :",n,end=">\n")
  print("sin",x)
  print("p",2**(n-1)*x)
print("with arctan",4.0*atan(1.0))