# n=5
# for i in range(1,n+1):
#     print(i)
    
# def func(n):
#     for i in range(1,n+1):
#         print(i)
# func(5)        
    
# def recursive(n, result=1):
#     if result > n:  
#         return
#     print(result)
#     recursive(n, result + 1)  

# recursive(5)
class RecursionTypes:
    def indirect_recursion(self,n):
        if n<=0:
            return
        print(f'Indirect recursion A:{n}')
        self.indirect_recursion_b(n-1)
    def indirect_recursion_b(self,n):
        if n<=0:
            return
        print(f'Indirect Recursion B:{n}')
        self.indirect_recursion_a(n-2)    
