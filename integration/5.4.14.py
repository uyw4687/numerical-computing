def f(x):
  return (1-x**2)**(-1/2)

left=5/9*f(-(3/5)**(1/2))
mid=8/9*f(0)
right=5/9*f((3/5)**(1/2))
print(left+mid+right)

weight_plus=0.5+1/12*(10/3)**(1/2)
weight_minus=0.5-1/12*(10/3)**(1/2)
node_plus=(1/7*(3+4*(0.3)**(1/2)))**(1/2)
node_minus=(1/7*(3-4*(0.3)**(1/2)))**(1/2)
left1=weight_plus*f(-node_minus)
left2=weight_minus*f(-node_plus)
right1=weight_plus*f(node_minus)
right2=weight_minus*f(node_plus)
print(left1+left2+right1+right2)