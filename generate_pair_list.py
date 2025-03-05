def unique_sorted_tuple(numbers):
    unique_numbers = sorted(set(numbers))  
    return tuple(unique_numbers)  
input_numbers = [4, 4, 44, 44]
output = unique_sorted_tuple(input_numbers)
print(output)  

def generate_pairs(lst):
    return [(lst[i], lst[i+1]) for i in range(len(lst)-1)]
numbers = [1, 2, 3]
output = generate_pairs(numbers)
print(output) 
