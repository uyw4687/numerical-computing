def f(x):
  return (x-1)*(x-3)*(x-5)
  # return x**2

a,b = 0,6
err = 10**-1

knots=[a]
knotsy=[f(a)]
finish=False

while knots[-1]!=b:

  obj,objy = b,f(b)

  while True:

    done=True

    prev,prevy = knots[-1],knotsy[-1]
    h,hy = (obj-prev)/10,(objy-prevy)/10
    curr,curry = prev,prevy

    for j in range(10):
      if abs(curry-f(curr))>err:
        done=False
        break
      curr+=h
      curry+=hy

    if done:
      break

    obj=(prev+obj)/2
    objy=f(obj)

  knots.append(obj)
  knotsy.append(f(obj))

print(len(knots))
print(knots)
print(knotsy)