lst = [44, 33, 3, 47, 54, 77, 999]
result = []
for i in range(len(lst) - 1):  
    sum = lst[i] + lst[i + 1]
    result.append(sum)
result.sort() 
print(result)
 