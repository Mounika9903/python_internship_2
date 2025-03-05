def binary_search_iterative(arr,x):
    left,right=0,len(arr)-1
    while left<=right:
        mid=left+(right-left)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            left=mid+1
        else:
            right=mid-1
    return -1 
arr=[3,5,6,7,8,9,12,45,66,]
x=12
print(binary_search_iterative(arr,x))


def binary_search_recursive(arr,left,right,x):
    if left>right:
        return-1
    mid=left+(right-left)//2
    if arr[mid]==x:
        return mid
    elif arr[mid]<x:
        return binary_search_recursive(arr,mid+1,right,x)
    else:
        return binary_search_recursive(arr,left,mid-1,x)       
arr=[3,5,6,7,89]
x=7
print(binary_search_recursive(arr,0,len(arr)-1,x) )   