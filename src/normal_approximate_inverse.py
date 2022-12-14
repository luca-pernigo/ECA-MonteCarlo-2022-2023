import numpy as np
x=np.random.uniform(0,1,10000)


def approximate_normal(u):
  a0= 2.50662823884
  a1= -18.61500062529
  a2= 41.39119773534
  a3= -25.44106049637

  b0= -8.47351093090 
  b1= 23.08336743743
  b2= -21.06224101826
  b3= 3.13082909833

  c0= 0.3374754822726147
  c1= 0.9761690190917186
  c2= 0.1607979714918209
  c3= 0.0276438810333863
  c4= 0.0038405729373609
  c5= 0.0003951896511919
  c6= 0.0000321767881768
  c7= 0.0000002888167364
  c8= 0.0000003960315187
  
  
  y=u-0.5
  if abs(y)<0.42:
    r=y*y
    x=y*(((a3*r+a2)*r+a1)*r+a0)/((((b3*r+b2)*r+b1)*r+b0)*r+1)
  else:
    r=u
    if(y>0):
      r=1-u
    r=np.log(-np.log(r))
    x=c0+r*(c1+r*(c2+r*(c3+r*(c4+r*(c5+r*(c6+r*(c7+r*c8)))))))
    if (y<0):
      x= -x   
  return x

approximate_normal_array = np.vectorize(approximate_normal)
arr = approximate_normal_array(x)
print(np.mean(arr))
print(arr)