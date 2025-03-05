def is_palindrome(s):
    return s == s[::-1]

def find_palindromic_substrings(s, targets):
    s = s.replace(" ", "") 
    found = []
    
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):  
            substr = s[i:j]
            if substr in targets and is_palindrome(substr):
                found.append(substr)
    
    return found
input_string = "azabayx"
target_substrings = {"aza", "abba"}
result = find_palindromic_substrings(input_string, target_substrings)
print("Found palindromic substrings:",result)
