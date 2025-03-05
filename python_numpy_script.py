# import numpy as np
# lists = np.array([[1, 2, 4], [4, 5, 6], [6, 7, 8]])
# for lst in lists:
#     print(lst)

arr1=[1,2,3,4,5,6]
arr2=[1,2,3],[4,5,6]
for i in range(len(arr2)):
    for j in range(len(arr2[i])):
        if(i==j or (i+j==2)):
            arr2[i][j]=0
        
        print(arr2[i][j],end=" ")
    print()            