class Employee:
    def __init__(self):
        print('Employee created')
    def __del__(self):
            print("Deconstructor called")
    def Create_obj():
        print('Making Object...')
        obj=Employee()
        print('function end...')
        return obj
print('Calling Create_obj() function...')
obj=Employee.Create_obj()
del obj
print('Program End...')