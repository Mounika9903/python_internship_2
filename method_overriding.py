class Parent:

    print("parent class")
class child(Parent):
    
    print("child class")
class Gchild(child):
    def show(self):
        print("Gchild class")
obj=Gchild()
obj.show()                