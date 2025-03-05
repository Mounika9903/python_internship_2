def traverse_stack(stack):
    if not stack:
        return
    element=stack.pop()
    print("Item popped")
    traverse_stack(stack)
    print(element)
stack=[1,2,3,4,5]
print("Stack elements:")
traverse_stack(stack)        