def f(v):
  return (1-v**2)**(-1/2)

a=-1
b=1

h=(b-a)/2
mid_y1=f((a+b)/2)
print('mid',2*h*mid_y1)
h=(b-a)/3
two_y1=f(a+h)
two_y2=f(b-h)
print('two',3*h/2*(two_y1+two_y2))
h=(b-a)/4
thr_y1=f(a+h)
thr_y2=f(a+2*h)
thr_y3=f(b-h)
print('three',4*h/3*(2*thr_y1-thr_y2+2*thr_y3))
h=(b-a)/5
four_y1=f(a+h)
four_y2=f(a+2*h)
four_y3=f(b-2*h)
four_y4=f(b-h)
print('four',5*h/24*(11*four_y1+four_y2+four_y3+11*four_y4))
h=(b-a)/6
five_y1=f(a+h)
five_y2=f(a+2*h)
five_y3=f(a+3*h)
five_y4=f(b-2*h)
five_y5=f(b-h)
print('five',6*h/20*(11*five_y1-14*five_y2+26*five_y3-14*five_y4+11*five_y5))