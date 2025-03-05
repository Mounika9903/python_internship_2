# import re
# def expand_string(s):
#     if not s:  
#         return ""
    
#     match = re.match(r"(\d+)([a-zA-Z])", s)  
#     if match:
#         num, char = int(match.group(1)), match.group(2)
#         return char * num + expand_string(s[match.end():])  
#     return ""  
# input_str = "3a4b1c"
# output_str = expand_string(input_str)
# print(output_str)  
def string(s, index=0, count=0):
    if index >= len(s):  
        return ""
    if s[index].isdigit():  
        count = count * 10 + int(s[index]) 
        return string(s, index + 1, count)
    return s[index] * count + string(s, index + 1, 0)
input_str = "3a4b1c"
output_str = string(input_str)
print(output_str)  

