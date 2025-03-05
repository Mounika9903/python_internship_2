def reverse_string(s):
    stack=list(s)
    reveresed_str= ""
    while stack:
        reveresed_str+=stack.pop()
    return reveresed_str
print(reverse_string("hello"))    