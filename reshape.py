import numpy as np
var3=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(var3)
print(var3.ndim)
x1=var3.reshape(2,3,2)
print(x1)
print(x1.ndim)

import numpy as np
var1=np.array([[[1,2,3,4],[1,2,3,4]]])
for k in var1:
    for n in k:
        for m in n:
            print(m)
            
import numpy as np
var=np.array([1,2,3,4])
var1=var.copy()
var[1]=40
print(var)
print(var1)       

import numpy as np
var=np.array([1,2,3,4,5,6,7,8])
x=np.searchsorted(var,5)
print(x)
     