class Final:
    def __init__(self):
        print("This class cannot be inherited")
    def funt1():
        return "hi"
    def __init_subclass__(cls,**kwargs):
        raise TypeError("Inheritance not allowed")
class Derived(Final):
    pass
obj=Derived()
print(obj.funt1())        