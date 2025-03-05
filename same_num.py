numbers = [44, 33, 3, 49, 54, 77, 999,4444,888888]
output = [num for num in numbers if num % 11 == 0 or (100 <= num <= 999)]
print(output)





lst=[44,33,47,54,77,999]
for i in lst:
    if i%11==0 or i%111==0:
        print(lst)