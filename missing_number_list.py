def find_missing_numbers(list):
    return [num for num in range(list[0], list[-1] + 1) if num not in list]

list = [1, 2, 4, 6, 7]
missing_numbers = find_missing_numbers(list)
print(missing_numbers)  
