def find_sublists_with_sum(list, target):
    result = []
    for i in range(len(list)):
        current_sum = 0
        for j in range(i, len(list)):
            current_sum += list[j]
            if current_sum == target:
                result.append(list[i:j+1])  
    return result
list = [1, 2, 3, 4, 5]
target = 5
print(find_sublists_with_sum(list, target))