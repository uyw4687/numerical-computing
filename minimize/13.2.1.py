from scipy.optimize import minimize

# def f(x):
#   a,b=x
#   return 100*(b-a**2)**2+(1-a)**2

# x=[-1.2, 1.0]

def f(v):
  x,y,z,w=v
  return 100*(x**2-y)**2+(1-x)**2+90*(z**2-w)**2+(1-z)**2+10*(y-1)**2+(w-1)**2+19.8*(y-1)*(w-1)

x=[-3, -1, -3, -1]
print(minimize(f,x,method='nelder-mead'))