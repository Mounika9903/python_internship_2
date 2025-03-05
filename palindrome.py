# def is_palindrome(s, left, right):
#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#     return True

# def palindrome_index(s):
#     left, right = 0, len(s) - 1
    
#     while left < right:
#         if s[left] != s[right]:
#             if is_palindrome(s, left + 1, right):
#                 return left
#             if is_palindrome(s, left, right - 1):
#                 return right
#             return -1
#         left += 1
#         right -= 1
        
#     return -1  # Already a palindrome

# # Example usage:
# s = input("Enter the string: ")
# print(palindrome_index(s))
# def longest_word(commentary):
#     words = commentary.split()
#     longest = ""
#     for word in words:
#         if len(word) > len(longest):
#             longest = word
#     return longest

# commentary = input("Enter cricket commentary: ")
# result = longest_word(commentary)
# print("Longest word:", result)
def is_palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def palindrome_index(s):
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:  
            if is_palindrome(s, left, right - 1):  # First check right side
                return right
            if is_palindrome(s, left + 1, right):  # Then check left side
                return left
            return -1  # More than one removal needed
        
        left += 1
        right -= 1
        
    return -1  # Already a palindrome

# Taking input from the user
s = input()
print(palindrome_index(s))