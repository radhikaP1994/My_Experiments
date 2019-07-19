import numpy as np
'''arr = np.array([[1,2,3,4,5,6],
               [1,2,3,4,5,6],
                [1,2,3,4,5,6]])'''
arr = np.array([[111,102,100,67,57,27],
               [22,21,13,7,3,2],
                [111,92,83,76,65,56]])
ds =np.sort(-arr)
ase = np.sort(arr)
an = ase  - arr
dn = ds + arr
if not dn.any() :
    print("DESC")
elif not an.any() :
    print("AESC")