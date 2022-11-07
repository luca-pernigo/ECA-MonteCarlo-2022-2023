import numpy as np
from numpy.linalg import eig

P = np.array([[0, 1, 0], 
              [0, 0.1, 0.9],
              [0.6, 0.4, 0]])
Pt=np.transpose(P)
Pt

w, v = np.linalg.eig(Pt)
  
# printing eigenvalues
print("eigenvalue 1:\n",
      w[0])
  
# printing eigenvectors
print("eigenvectors with eigenvalue 1:\n", v[:,0]) 

v=v[:,0]
v=v/np.sum(v)
v
