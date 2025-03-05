def cumulative_sum(lst):
    result=[]
    total=0
    for num in lst:
        total+=num
        result.append(total)
    return result
print(cumulative_sum([1,2,3,4]))
