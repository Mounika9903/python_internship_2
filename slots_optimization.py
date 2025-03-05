class Person:
    __slots__=['name','age']
    def __init__(self,name,age):
        self.name=name
        self.age=age
p= Person('Raja',30)
print(f"{p.name},{p.age}")
p.name='Rohit'
print(f"{p.name},{p.age}")        