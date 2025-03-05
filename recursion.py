# def sum_list(list):
#     if not list:  
#         return 0
#     return list[0] + sum_list(list[1:])  

# list = [1, 2, 3, 4, 5]
# print(sum_list(list)) 
input_string="bz"
input_string2="bbz"
alcount=[]
for i in range(97,123):
    char=chr(i)
    print(char)
    count=input_string.count(char)
    alcount.append(count)
print(alcount)    