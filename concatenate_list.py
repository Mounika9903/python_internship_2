def concatenate_lists(list1,list2):
    result=[]
    for i in range(max(len(list1),len(list2))):
        result.append(list1[i]+list2[i])
        return result
print(concatenate_lists(['h','f','y'],['i','i']))